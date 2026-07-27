#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Generate the labs/ markdown from the SAME single source as the deck/LP/LG
(course_data.py + data_domainN.py), so labs stay 100% aligned with the other
artifacts. Emits labs/lab-NN-*.md, labs/README.md and refreshes nothing else
(tools.md and the brief pack are hand-authored). Enrichment sections
(Prerequisites, Troubleshooting, Challenge, Reflection, Deliverable) live in the
ENRICH table below, keyed by lab number.

Run:  python gen_labs.py
"""
import os, re, sys, glob, importlib

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import course_data as C


def find_repo(start):
    env = os.environ.get("COURSE_REPO")
    if env and os.path.isdir(env):
        return env
    d = start
    for _ in range(8):
        d = os.path.dirname(d)
        if os.path.isdir(os.path.join(d, "courseware")) and os.path.isdir(os.path.join(d, "labs")):
            return d
    return os.path.dirname(os.path.dirname(start))


REPO = find_repo(HERE)
LABS = os.path.join(REPO, "labs")

# ------------------------------------------------------------------ load labs
DOMS = []
for f in sorted(glob.glob(os.path.join(HERE, "data_domain[0-9]*.py"))):
    mod = importlib.import_module(os.path.splitext(os.path.basename(f))[0])
    key = [k for k in dir(mod) if k.startswith("DOMAIN")][0]
    DOMS.append((getattr(mod, key), getattr(mod, "SCENARIO", None)))

LABSLIST = []
SCENARIO = None
for dom, scen in DOMS:
    if scen and not SCENARIO:
        SCENARIO = scen
    LABSLIST.extend(dom)

TOPIC_TITLE = {t["num"]: t["title"] for t in C.TOPICS}

# ------------------------------------------------------------------ approx minutes per lab
# Derived from the schedule lab blocks so the labs match the Lesson Plan timing.
def lab_titles(nums):
    return "; ".join("" for _ in nums)


def approx_minutes():
    sched = C.SCHEDULE(lambda nums: "\x00".join(str(n) for n in nums))
    mins = {}
    for _day, (_theme, rows) in sched.items():
        for row in rows:
            if row[3] == "lab":
                nums = [int(x) for x in row[4].split("Hands-on: ")[-1].split("\x00")]
                per = round(row[2] / len(nums))
                for n in nums:
                    mins[n] = per
    return mins


MINS = approx_minutes()

# ------------------------------------------------------------------ per-lab enrichment
ENRICH = {
 1: dict(
    prereqs=[
        "A laptop able to run the current release of Adobe Photoshop, with an internet connection.",
        "Adobe Photoshop installed and updated to a version with Generative Fill, and signed in to your Adobe account.",
        "Firefly generative credits available on your account (check your balance before you start).",
    ],
    trouble=[
        "**No 'Generative Fill' button appears.** Make an active selection first (the Contextual Task Bar only shows Generative Fill when something is selected), and confirm Photoshop is updated and you are signed in.",
        "**Generation fails or says you're out of credits.** Check your internet connection and your Firefly generative-credit balance in your Adobe account; the features process in the cloud.",
        "**The result looks wrong or pasted-on.** That is fine for a first try — you learn to prompt and select better in the next labs. For now, just learn the loop and the variations.",
    ],
    challenge="Run the same simple fill with a very different style word (for example 'watercolour' vs 'photorealistic') and compare — notice how much one word changes the result.",
    lo=1,
    deliverable="Keep 'solace-hero.psd' (back to the clean serum photo) and your one-line note on the generate–review–refine loop — your warm-up before the real campaign work.",
 ),
 2: dict(
    prereqs=[
        "Completed Lab 1 (you can run a Generative Fill and review variations).",
        "The supplied Solace reference pack open (labs/reference-pack/).",
    ],
    trouble=[
        "**The fill ignores part of the prompt.** Keep prompts concise and put the subject first; iterate with small changes rather than piling on more words.",
        "**You get an instruction-like result.** Describe what you WANT to see in the area ('a cream surface with soft shadows'), not a command ('remove the shadows').",
        "**Unwanted extras appear (text, logos, clutter).** Add a short negative cue and regenerate.",
    ],
    challenge="Write a structured prompt for a completely different product of your own using the same five slots, proving the template works beyond the serum.",
    lo=2,
    deliverable="Keep your final Solace prompt and the reusable prompt template — you reuse them in Labs 3, 6 and 7.",
 ),
 3: dict(
    prereqs=[
        "Completed Lab 2 (you have a strong Solace prompt and template).",
        "'solace-hero.psd' open with the clean serum photo.",
    ],
    trouble=[
        "**The added prop's light doesn't match.** State the light direction in the prompt ('soft daylight from the left, gentle shadow') and regenerate, or adjust the selection size.",
        "**The removed object leaves a smudge or ghost.** Re-select with a little more margin and generate again with an empty prompt; a snug but not tight selection fills cleanest.",
        "**The edit looks pasted-on at the edges.** Nudge the selection, regenerate, or add a layer mask and soften the join.",
    ],
    challenge="Add two different props on separate generative layers, then show/hide them to offer the client alternative compositions from one file.",
    lo=3,
    deliverable="Keep 'solace-hero.psd' with a prop added and a distraction removed on clearly named generative layers — the base for the expand and background labs.",
 ),
 4: dict(
    prereqs=[
        "Completed Lab 3 (a cleaner hero shot with added/removed content).",
        "The Crop tool and Generative Expand available in your Photoshop version.",
    ],
    trouble=[
        "**A visible seam or repeat appears in the new area.** Expand in two smaller steps instead of one big drag, and regenerate; state 'continue the same surface' in the prompt.",
        "**The generated space adds unwanted objects.** Add a short negative cue ('empty, uncluttered, room for text') or leave the prompt empty to simply continue the scene.",
        "**The bottle ends up centred with no room for a headline.** Re-crop so the bottle sits on one third and the empty canvas is on the other side.",
    ],
    challenge="Reformat the same hero into a tall story format (9:16) as well as the wide banner, proving one image can serve every placement.",
    lo=4,
    deliverable="Keep 'solace-banner.psd' — a wide, well-composed banner with generated space and clear room for a headline.",
 ),
 5: dict(
    prereqs=[
        "Completed Lab 4 (hero and banner in progress).",
        "The Remove tool available (grouped with the Spot Healing / retouch tools).",
    ],
    trouble=[
        "**The Remove tool leaves a blur or artefact.** Undo and use a slightly larger brush, or a couple of small strokes; size the brush to the mark, not the whole area.",
        "**A larger object won't clean up well.** Switch to a Generative Fill with a selection (Lab 3) — the Remove tool is best for small tidy-ups.",
        "**Your cleanup edits the original pixels.** Work on a new blank layer with 'Sample all layers' on so the edits stay non-destructive.",
    ],
    challenge="Time yourself cleaning the same distraction with the Remove tool versus a Generative Fill selection, and note which is faster for which size of job.",
    lo=5,
    deliverable="Keep the cleaned 'solace-hero.psd' and 'solace-banner.psd' — blemish-free, with cleanups on a non-destructive layer.",
 ),
 6: dict(
    prereqs=[
        "Completed Lab 5 (clean hero and banner).",
        "Your reusable Solace prompt from Lab 2 for describing the new scene.",
    ],
    trouble=[
        "**The bottle looks cut out against the new background.** Refine the selection edge in Select and Mask (smooth, slightly feather), especially around the cap and glass.",
        "**The background light fights the product.** State the light direction explicitly ('daylight from the left') and regenerate so shadows fall the same way as on the bottle.",
        "**The product looks like it's floating.** Add a small contact shadow with a low Generative Fill selection or a soft brush on a Multiply layer.",
    ],
    challenge="Generate three different backgrounds (studio, botanical, stone ledge) on separate layers and present them as a mini set of options.",
    lo=6,
    deliverable="Keep 'solace-hero.psd' with the serum in a new, coherent scene and an alternative background layer alongside — ready to composite.",
 ),
 7: dict(
    prereqs=[
        "Completed Lab 6 (the product on a replaced background).",
        "Your Lab 2 prompt and a reference image you are authorised to use (see the reference pack).",
    ],
    trouble=[
        "**The scene ignores your reference.** Confirm the reference image is attached in the generate panel and try a stronger match; a clean, single-subject reference steers best.",
        "**The result looks like art, not a photo.** Set the content type to Photo (not Art) and choose a realistic style, then regenerate.",
        "**The light won't match your hero bottle.** Set the lighting so it comes from the same side as your product (left), so the pieces composite together later.",
    ],
    challenge="Generate the same scene with two different styles (for example 'warm film photo' vs 'clean editorial') and keep both as mood options for the client.",
    lo=7,
    deliverable="Keep the chosen lifestyle scene placed into your project as a 'lifestyle-scene' layer, with its Content Credentials and settings noted for the IP check.",
 ),
 8: dict(
    prereqs=[
        "Completed Lab 7 (a lifestyle scene in the project).",
        "The supplied 'solace-model.jpg' (or your own photo of a person who has consented to being edited).",
    ],
    trouble=[
        "**Skin looks plastic after Skin Smoothing.** Lower the Blur and Smoothness sliders until natural skin texture returns; subtle beats heavy.",
        "**A Neural Filter changes the person too much.** Discard it — for a premium brand keep edits realistic; Smart Portrait tweaks should be barely noticeable or not used.",
        "**The retouch edits the original photo.** Duplicate the background layer first and output each Neural Filter to its own new layer so everything stays non-destructive.",
    ],
    challenge="Do a light and a heavy retouch of the same portrait, put them side by side, and decide where 'natural' ends — the judgement matters more than the sliders.",
    lo=8,
    deliverable="Keep 'solace-model.psd' — a naturally retouched portrait on non-destructive layers, with the consent/likeness note recorded.",
 ),
 9: dict(
    prereqs=[
        "Completed Lab 8 (a retouched portrait) and Labs 3–7 (product, background, scene, props).",
        "All the pieces available in one Photoshop document or ready to place.",
    ],
    trouble=[
        "**An element looks pasted on.** Add or refine its layer mask with a soft brush, and match its colour with a clipped adjustment layer — mismatched colour is the usual giveaway.",
        "**A shadow covers the surface in grey.** Put the shadow on its own layer set to Multiply so it darkens rather than paints over.",
        "**Highlights look like stickers.** Paint them on a Screen or Overlay layer and lower the opacity so they read as real light.",
    ],
    challenge="Rebuild the composite with the light coming from the other side, re-matching every shadow and highlight — proof you control the blend, not luck.",
    lo=9,
    deliverable="Keep the layered, grouped composite PSD — product, scene, light and colour blended so it reads as one photograph.",
 ),
 10: dict(
    prereqs=[
        "Completed Lab 9 (a finished composite).",
        "Access to Adobe's current generative-AI usage terms and your generative-credit balance.",
    ],
    trouble=[
        "**Export looks different from the canvas.** Export a flattened COPY (never your master PSD) at high quality, and check the colour profile matches your document.",
        "**Reformatting crops out the product.** Use Generative Expand (Lab 4) to add canvas rather than cropping in, then reposition the product for each format.",
        "**Unsure whether you can use an element commercially.** If you can't confirm the rights to a non-Firefly image, person or brand, remove or replace it before publishing.",
    ],
    challenge="Write a one-paragraph 'AI disclosure' line for this campaign that you would be comfortable publishing alongside the visual.",
    lo=10,
    deliverable="Keep the finished master PSD, the three exported formats and the completed commercial-use / IP checklist — your publishable, cleared deliverable.",
 ),
}


def slug(title):
    s = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    if len(s) > 60:
        s = s[:60].rstrip("-")
    return s


def steps_md(steps):
    out = []
    for i, (instr, cmd) in enumerate(steps, 1):
        out.append(f"### Step {i}\n\n{instr}")
        if cmd:
            out.append("Text to use (paste into Photoshop's Generative Fill / generate box):\n\n```text\n" + cmd + "\n```")
    return "\n\n".join(out)


def lab_filename(lab):
    return f"lab-{lab['num']:02d}-{slug(lab['title'])}.md"


def build_lab(lab):
    e = ENRICH[lab["num"]]
    topic = lab["topic"]
    mins = MINS.get(lab["num"], 40)
    parts = []
    parts.append(f"# Lab {lab['num']} — {lab['title']}\n")
    parts.append(
        f"**Topic 0{topic}:** {TOPIC_TITLE[topic]}  |  **Day 1**  |  "
        f"**Approx. {mins} min**  |  **Course:** {C.TITLE}\n"
    )
    if SCENARIO:
        parts.append("## Scenario\n\n" + SCENARIO + "\n")
    parts.append("## Goal\n\n" + lab["objective"] + "\n")
    parts.append("## What you'll build\n\n" + lab["build"] + "\n")
    parts.append("**Tools and techniques:** " + lab["services"] + "\n")
    parts.append("## Prerequisites\n\n" + "\n".join("- " + p for p in e["prereqs"]) + "\n")
    parts.append("## Steps\n\n" + steps_md(lab["steps"]) + "\n")
    parts.append("## Test it\n\n" + lab["test"] + "\n")
    parts.append("## Troubleshooting\n\n" + "\n".join("- " + t for t in e["trouble"]) + "\n")
    parts.append("## Challenge\n\n" + e["challenge"] + "\n")
    lo = C.LEARNING_OUTCOMES[e["lo"] - 1]
    lo_text = lo.split(":", 1)[1].strip().rstrip(".")
    parts.append(f"## Reflection\n\nLO{e['lo']} — In your own words: {lo_text}?\n")
    parts.append("## Deliverable\n\n" + e["deliverable"] + "\n")
    parts.append("---\n")
    parts.append(
        f"*{C.TITLE} · {C.COURSE_CODE} · Version {C.VERSION} · © 2026 {C.ORG}*"
    )
    return "\n".join(parts) + "\n"


def build_readme(files):
    rows = []
    for lab in LABSLIST:
        fn = files[lab["num"]]
        rows.append(
            f"| 1 | 0{lab['topic']} | {lab['num']:02d} | [{lab['title']}]({fn}) |"
        )
    md = []
    md.append(f"# Labs — {C.TITLE}\n")
    md.append(f"**Course Code:** {C.COURSE_CODE}  |  **Version {C.VERSION} · {C.VERSION_DATE}**\n")
    md.append(
        "All 10 labs build one connected **Solace Radiance Serum campaign key visual**, which you begin in "
        "Lab 1 and finish in Lab 10 — from writing effective prompts, through Generative Fill, Generative "
        "Expand, the AI Remove tool and background replacement, into text-to-image, portrait retouching and a "
        "masked, blended composite, and out as a finished, exported deliverable checked for commercial use. "
        "A Solace reference pack and starter files are supplied in `reference-pack/` and `starter-files/`; use "
        "your own non-confidential product wherever you prefer. There is **no assessment** — each lab verifies "
        "itself with a 'Test it' step.\n"
    )
    md.append("| Day | Topic | Lab | Title |")
    md.append("|---:|---|---:|---|")
    md.extend(rows)
    md.append("")
    md.append("## Tools\n")
    md.append("See [tools.md](tools.md) for the accounts and tools used across the labs, and "
              "[reference-pack/](reference-pack/) for the sample object.")
    return "\n".join(md) + "\n"


def main():
    os.makedirs(LABS, exist_ok=True)
    # remove stale lab-*.md so renamed labs don't linger
    for old in glob.glob(os.path.join(LABS, "lab-*.md")):
        os.remove(old)
    files = {}
    for lab in LABSLIST:
        fn = lab_filename(lab)
        files[lab["num"]] = fn
        with open(os.path.join(LABS, fn), "w", encoding="utf-8") as fh:
            fh.write(build_lab(lab))
        print("wrote labs/" + fn)
    with open(os.path.join(LABS, "README.md"), "w", encoding="utf-8") as fh:
        fh.write(build_readme(files))
    print("wrote labs/README.md")


if __name__ == "__main__":
    main()
