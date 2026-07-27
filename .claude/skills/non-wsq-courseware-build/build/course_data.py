"""
SINGLE SOURCE OF TRUTH — C16 Generative AI for Adobe Photoshop (non-WSQ).

An intensive, one-day, hands-on course on transforming image-editing workflows
with the generative AI built into Adobe Photoshop (Adobe Firefly). Learners write
effective prompts and use Generative Fill, Generative Expand, the AI Remove tool
and background generation to edit photos non-destructively; they then move into
advanced workflows — text-to-image with reference images and styles, AI portrait
retouching and Neural Filters, and compositing generative layers with masks and
blend modes — to build a complete, end-to-end generative design, ending with the
commercial-use and intellectual-property considerations that govern real work.
Every artifact (PPT, LP, LG, LG.md) and every lab is generated from this module +
data_domainN.py so they stay 100% aligned.

NON-WSQ RULES — the engine enforces these, do not reintroduce them here:
  * NO assessment of any kind (no WA/SAQ, no PP, no case study, no marking).
  * NO SSG / SkillsFuture / WSQ funding or subsidy content.
  * NO TRAQOM survey, NO digital attendance, NO 75% attendance rule.
  * NO TGS course reference — this course carries the plain code C16.
"""

# ------------------------------------------------------------------ metadata
TITLE        = "Generative AI for Adobe Photoshop (C16)"
SHORT_TITLE  = "Generative AI for Adobe Photoshop (C16)"   # used in output filenames
COURSE_CODE  = "C16"                                        # non-WSQ code — never a TGS- ref
VERSION      = "v1.0"
VERSION_DATE = "27 July 2026"
ORG          = "Tertiary Infotech Academy Pte Ltd"
UEN          = "UEN: 201200696W"
TRAINER      = "Dr. Alfred Ang"
DAYS         = 1
MODE         = "Instructor-led, hands-on practical labs"

DARK_THEME = False

# ------------------------------------------------------------------ outcomes
LEARNING_OUTCOMES = [
    "LO1: Describe how generative AI (Adobe Firefly) works inside Photoshop and navigate the generate–review–refine loop using the Contextual Task Bar and generative layers.",
    "LO2: Write effective, structured prompts that control subject, style and detail for image generation in Photoshop.",
    "LO3: Add and remove content non-destructively with Generative Fill and generative layers.",
    "LO4: Extend an image beyond its original canvas with Generative Expand to re-compose and re-format it.",
    "LO5: Clean up an image in one click with the AI Remove tool to erase distractions and blemishes.",
    "LO6: Generate and replace a background to place a subject in a new, coherent scene.",
    "LO7: Generate images from text using reference images and styles to control the look of a result.",
    "LO8: Retouch portraits with AI — generative retouching and Neural Filters — naturally and ethically.",
    "LO9: Combine generative layers with masks and blend modes to composite a polished final image.",
    "LO10: Build an end-to-end generative design workflow and apply commercial-use and intellectual-property considerations to AI-generated visuals.",
]
LO_TITLES = [
    "Firefly in Photoshop",
    "Prompting",
    "Generative Fill",
    "Generative Expand",
    "AI Remove",
    "Backgrounds",
    "Text-to-Image",
    "Portrait retouch",
    "Compositing",
    "Workflow & IP",
]

# ------------------------------------------------------------------ topics
# `concepts` are plain strings ("Title — explanation.") so they render cleanly
# as both slide tiles and Learner-Guide bullets. `weighting` = share of course time.
TOPICS = [
    dict(num=1, code="01",
         title="Generative Editing Essentials in Photoshop",
         subtitle="Introduction to Adobe Firefly and generative AI in Photoshop · Writing effective prompts for image generation · Adding and removing content with Generative Fill · Extending images with Generative Expand · One-click cleanup with the AI Remove tool · Generating and replacing backgrounds",
         weighting="60%",
         concepts=[
            "Adobe Firefly and generative AI in Photoshop — Firefly is Adobe's image-generation model, built into Photoshop so you can add, remove, extend and reimagine parts of a photo by describing them in words, right on the canvas, without leaving the app.",
            "The Contextual Task Bar and the generate–review–refine loop — you make a selection, type a short prompt (or leave it blank), and Photoshop generates several variations; you review them, then regenerate or refine until one is right. This loop is the heart of every generative edit.",
            "Generative layers are non-destructive — every generative result lands on its own generative layer above your photo, so the original pixels are never touched; you can hide, re-generate, mask or delete a result at any time without harming the image underneath.",
            "Variations and generation credits — each generate produces three variations to choose from, and you can keep generating for more; generations use Firefly generative credits, so part of the craft is getting a strong result in fewer tries with a better selection and prompt.",
            "Writing effective prompts — a good prompt names the subject, adds a few descriptive details and, where it helps, a style; you describe what you WANT to see in the selected area (not an instruction like 'remove this'), keep it concise, and iterate rather than over-loading one prompt.",
            "Generative Fill to add and remove content — select an area and describe something to insert it seamlessly matched to the photo's light and perspective; select an object and generate with an empty prompt to remove it and fill the gap with a believable background.",
            "Generative Expand — enlarge the canvas with the Crop tool and Photoshop generates new image to fill the added space, so you can re-frame a subject, straighten a crooked shot, or reformat a square photo into a wide banner or a tall story, all in one step.",
            "The AI Remove tool — a brush-based one-click cleanup that erases distractions, blemishes, wires or stray objects and intelligently reconstructs what should be behind them, faster than a manual selection for small tidy-ups.",
            "Generating and replacing backgrounds — select the subject, invert the selection (or use Select Subject / Remove Background), then use Generative Fill to place the subject into a completely new, described scene whose lighting and perspective match the subject.",
         ]),
    dict(num=2, code="02",
         title="Advanced Generative Workflows",
         subtitle="Text-to-image generation with reference images and styles · AI-powered portrait retouching and Neural Filters · Combining generative layers with masks and blend modes · Building end-to-end generative design workflows · Commercial use and intellectual-property considerations",
         weighting="40%",
         concepts=[
            "Text-to-image generation — beyond editing an existing photo, you can generate a brand-new image from a text prompt (in Photoshop's generate workflow or in the Firefly web app) to create concepts, backgrounds and lifestyle scenes from nothing but a description.",
            "Reference images and style controls — you steer a generated image's look by supplying a reference image (to match composition or subject) and by choosing a style, content type (photo vs art), effects, colour and lighting, so results stay on-brand instead of random.",
            "AI-powered portrait retouching — generative retouching and the Remove/Fill tools clean skin, remove flyaway hair and stray objects and even adjust eyes or expression on a portrait, quickly and non-destructively, while keeping the person looking natural.",
            "Neural Filters — a panel of AI-powered filters (Skin Smoothing, Smart Portrait, Colorize, Style Transfer, Landscape Mixer and more) that apply sophisticated, model-driven edits from simple sliders, each output kept on its own layer.",
            "Masks with generative layers — a layer mask hides or reveals part of a generative layer with black-and-white painting, so you blend a generated element precisely into the scene and control exactly where it shows.",
            "Blend modes — a blend mode changes how a generative layer's pixels combine with the layers below (Multiply, Screen, Overlay, Soft Light and others), letting you merge light, shadow, colour and texture so a composite reads as one photograph.",
            "End-to-end generative design workflow — real work chains these tools together: generate or edit the subject, expand and re-frame, replace the background, retouch, then composite generative layers with masks and blend modes into one finished, layered deliverable you can revise.",
            "Commercial use and licensing — Firefly is designed to be commercially safe (trained on licensed and public-domain content), but you must still check Adobe's current generative-AI usage terms, any credit limits, and the rights to every non-Firefly image, model or brand you bring in.",
            "Intellectual property and responsible use — you own your prompts and your edits, but you must respect other people's copyright, trademarks and likeness; disclose AI use where required, avoid deceptive edits, and note that Firefly can attach Content Credentials (provenance metadata) to a result.",
         ]),
]

# ------------------------------------------------------------------ day themes
DAY_THEMES = {
    1: "Build a complete brand campaign key visual for the Solace Radiance Serum using generative AI in Photoshop — from prompting, Generative Fill, Generative Expand, AI Remove and background replacement to text-to-image, portrait retouching and a masked, blended final composite — and finish with the commercial-use and IP checks that govern real work",
}

# ------------------------------------------------------------------ schedule
# NON-WSQ: no assessment blocks. The day runs 9:00–18:00 (540 min) minus a 1-hour
# lunch = 480 scheduled minutes; the 30 minutes of tea breaks sit inside that, so
# the instructional total is 7.5 hours.
def SCHEDULE(lab_titles):
    return {
     1: (DAY_THEMES[1], [
        ("9:00","9:20",20,"admin","Welcome, course introduction, ground rules, and setup: launching Photoshop with the latest generative features, signing in to an Adobe account with Firefly credits, and opening the supplied Solace starter files for the labs"),
        ("9:20","10:00",40,"topic","TOPIC 01 — Generative Editing Essentials in Photoshop: introduction to Adobe Firefly and generative AI in Photoshop; writing effective prompts; adding and removing content with Generative Fill; extending images with Generative Expand; one-click cleanup with the AI Remove tool; generating and replacing backgrounds (concepts + live demo)"),
        ("10:00","10:45",45,"lab","Hands-on: "+lab_titles([1,2])),
        ("10:45","11:00",15,"break","Tea break"),
        ("11:00","13:00",120,"lab","Hands-on: "+lab_titles([3,4,5])),
        ("13:00","14:00",60,"lunch","Lunch break"),
        ("14:00","14:40",40,"lab","Hands-on: "+lab_titles([6])),
        ("14:40","15:10",30,"topic","TOPIC 02 — Advanced Generative Workflows: text-to-image with reference images and styles; AI-powered portrait retouching and Neural Filters; combining generative layers with masks and blend modes; building end-to-end generative design workflows; commercial use and intellectual-property considerations (concepts + live demo)"),
        ("15:10","16:15",65,"lab","Hands-on: "+lab_titles([7,8])),
        ("16:15","16:30",15,"break","Tea break"),
        ("16:30","17:50",80,"lab","Hands-on: "+lab_titles([9,10])),
        ("17:50","18:00",10,"recap","Course wrap-up, exporting the campaign key visual, commercial-use and IP recap, responsible use and next steps"),
     ]),
    }

# ------------------------------------------------------------------ deck content
COURSE_OVERVIEW = dict(
    section_title="Course Fundamentals",
    concepts_title="What Generative AI in Photoshop Really Is",
    concepts=[
        "Editing by describing — instead of cloning, masking and painting every pixel by hand, you select an area and describe what you want, and Adobe Firefly generates it directly into your photo, matched to its light and perspective.",
        "Non-destructive by design — every generative result lands on its own layer, so the original photo is untouched and you can re-generate, mask or delete any edit at any time.",
        "One skill, the whole toolset — the same generate–review–refine loop drives Generative Fill, Generative Expand, background replacement, text-to-image and portrait retouching.",
        "From edit to end-to-end design — the real power is chaining these tools into one workflow that takes a plain product photo all the way to a finished, layered campaign visual.",
    ],
    framework_title="The Generative Photoshop Workflow",
    framework=[
        ("Prompt", "Describe the subject, detail and style you want — for a fill, an expand, a new background or a whole image."),
        ("Generate", "Firefly produces variations on their own generative layers, matched to the photo's light and perspective."),
        ("Review", "Compare the variations, keep the strongest, and re-generate or refine the prompt and selection for the rest."),
        ("Composite", "Blend the generative layers with masks and blend modes so everything reads as one photograph."),
        ("Deliver", "Export the finished, layered key visual — and check commercial-use and IP before it ships."),
    ],
    statement=dict(
        headline="Generative AI gives you a believable edit in seconds — the craft is a clean selection, a clear prompt, and a careful composite.",
        body="This course is hands-on: you take one hero product — the Solace Radiance Serum — from a plain photo through fill, expand, cleanup, background replacement, text-to-image, portrait retouching and compositing into one finished brand campaign key visual.",
        kicker="THE WORKFLOW RULE",
    ),
    pillars_title="What You'll Build",
    pillars=[
        ("A clean hero shot", ["A strong reusable prompt", "Added and removed content with Generative Fill", "A one-click AI Remove cleanup"]),
        ("A reformatted image", ["A wide banner via Generative Expand", "A re-composed, straightened frame", "A newly generated background"]),
        ("Advanced generative art", ["A text-to-image lifestyle scene", "Reference-image and style control", "An AI-retouched portrait"]),
        ("A finished campaign visual", ["A masked, blended composite", "An end-to-end layered file", "A commercial-use / IP check"]),
    ],
    arc_title="How Every Lab Works",
    arc=[
        "The trainer demonstrates the technique on the shared Solace serum example.",
        "You build it yourself in your own Photoshop using the supplied Solace starter files and reference pack.",
        "You verify the result against the lab's explicit 'Test it' check.",
        "You refine the result — re-generate, adjust the selection, or mask and blend — until it meets the brief.",
        "You keep the finished layered file — it becomes the next stage of your Solace campaign visual.",
    ],
)

# ------------------------------------------------------------------ LG content
LG_INTRO = (
    "This Learner Guide accompanies the Generative AI for Adobe Photoshop (C16) course, conducted by "
    "Tertiary Infotech Academy Pte Ltd. It carries the full detail of all 10 hands-on labs, in the "
    "order you will run them, together with the concepts each lab depends on."
)
LG_INTRO2 = (
    "The labs build a single, connected deliverable — a brand campaign key visual for the Solace Radiance "
    "Serum, a fictional botanical skincare product from the studio Aster & Vale. You start in Lab 1 by "
    "getting oriented in Photoshop's generative tools, then in every lab you take the campaign one stage "
    "further — a strong prompt, added and removed content with Generative Fill, a Generative Expand banner, "
    "an AI Remove cleanup, a replaced background, a text-to-image lifestyle scene, an AI-retouched portrait, "
    "and finally a masked, blended composite you finish and check for commercial use. A reference pack and "
    "starter files are supplied; you may substitute your own non-confidential product wherever you prefer."
)
LG_SETUP = dict(
    needs=[
        "A laptop (Windows or Mac) able to run the current release of Adobe Photoshop — a reasonably recent machine with 8 GB RAM minimum, 16 GB preferred.",
        "Adobe Photoshop installed and updated to a version with Generative Fill, Generative Expand and the Remove tool (a free trial is available from adobe.com). The trainer will confirm the version at the start of the day.",
        "An Adobe account signed in to Photoshop, with Firefly generative credits available — the labs stay within a modest number of generations, but check your credit balance before you start.",
        "An internet connection — the generative features process in the cloud, so they need to be online.",
        "The supplied Solace starter files and reference pack (a product photo, a portrait, a prompt sheet and style notes) — or a few photos and notes for your own non-confidential product to use instead.",
    ],
    verify_text="Before Lab 1, confirm Photoshop opens, that you can see the Contextual Task Bar with a 'Generative Fill' button when you make a selection, and that you are signed in to your Adobe account with credits available. If anything is missing, tell the trainer.",
    verify_code="Open Photoshop  ·  make a selection and confirm the Contextual Task Bar shows Generative Fill  ·  check Firefly credits in your Adobe account",
    conventions=[
        "Placeholders such as <YOUR PRODUCT> or <YOUR REFERENCE IMAGE> are replaced with your own values.",
        "Prompts to type into Photoshop's Generative Fill or generate box are shown in the 'Text to use' blocks — adapt them to your own product.",
        "Every lab ends with a 'Test it' step — an explicit check that the result meets the brief before you move on.",
        "Keep every file for one campaign in a single project folder, and save layered PSDs so your work stays non-destructive and editable.",
    ],
)
LAB_NOTE = (
    "Use only images, people and brands you are authorised to use. Do not upload a real company's product photo, a "
    "copyrighted image, or a photo of a person without their consent, and check Adobe's current generative-AI usage "
    "terms before you publish or sell a result. Use the supplied Solace starter files rather than confidential "
    "material, and note that generative features process your images in the cloud under Adobe's terms of service."
)
LG_WRAPUP = dict(
    title="Wrap-Up",
    intro="You have taken one hero product — the Solace Radiance Serum — through the entire generative-AI workflow in Photoshop in a single day, from a plain product photo and a clear prompt to a finished, layered brand campaign key visual, and checked it for commercial use and IP.",
    sections=[
        dict(title="What you built", bullets=[
            "A strong, reusable prompt that controls subject, style and detail for generative edits and image generation.",
            "A clean hero shot with content added and removed by Generative Fill and a one-click AI Remove cleanup.",
            "A wide banner produced with Generative Expand, and a completely replaced, coherent background.",
            "A text-to-image lifestyle scene steered by a reference image and style controls, and an AI-retouched portrait.",
            "A masked, blended composite assembled into one end-to-end layered campaign key visual, checked for commercial use and IP.",
        ]),
        dict(title="What to do next", bullets=[
            "Rebuild the campaign for a real, non-confidential product of your own using the same prompt template and workflow.",
            "Export the key visual in the formats a real campaign needs — a wide web banner, a square social post and a tall story — reusing your Generative Expand skills.",
            "Keep your prompt sheet and layered PSD as reusable templates so future visuals follow the same clean, non-destructive workflow.",
            "Always check Adobe's generative-AI usage terms and the rights to every image, person and brand, and disclose AI assistance where appropriate before you publish or sell.",
        ]),
    ],
)
LG_NEXT_STEPS = [
    "First pass: complete every lab yourself, following the steps and verifying each 'Test it' check.",
    "Second pass: rebuild the key visual from your prompt and starter photo alone, compositing it without the step-by-step.",
    "Apply the workflow to a real, non-confidential product or brand of your own.",
    "Review each lab's detailed steps in this guide and re-create the campaign in your own Photoshop.",
]
LG_GLOSSARY = [
    ("Generative AI", "AI that creates new content — here, images — from a text prompt or an existing image, rather than only filtering pixels that already exist."),
    ("Adobe Firefly", "Adobe's generative image model, built into Photoshop, that powers Generative Fill, Generative Expand, background generation and text-to-image."),
    ("Generative Fill", "A Photoshop feature that generates content into a selected area from a text prompt — to add an object, or (with an empty prompt) to remove one and fill the gap."),
    ("Generative Expand", "Enlarging the canvas with the Crop tool so Photoshop generates new image to fill the added space, used to re-frame, straighten or reformat a photo."),
    ("Generative layer", "The special layer each generative result lands on, keeping the edit non-destructive and separately editable, re-generatable and maskable."),
    ("Contextual Task Bar", "The floating bar that appears near your selection offering the right next action — such as Generative Fill — so you work directly on the canvas."),
    ("Variations", "The set of results (three at a time) Photoshop returns for each generation, shown in the Properties panel so you can pick the best or generate more."),
    ("Generative credits", "Firefly's usage allowance; each generation consumes credits, so a good selection and prompt that get a result in fewer tries are part of the craft."),
    ("Prompt", "The text you type to describe what you want generated; describe what you WANT to see in the area, concisely, and iterate rather than over-loading one prompt."),
    ("Reference image", "An image you supply to steer a text-to-image result toward a particular composition, subject or look, instead of relying on words alone."),
    ("Style / content type", "Firefly controls that set whether a result is a photo or art and apply a visual style, effects, colour and lighting to keep it on-brand."),
    ("Remove tool (AI Remove)", "A brush-based Photoshop tool that erases a distraction or blemish in a stroke and reconstructs what should be behind it."),
    ("Select Subject / Remove Background", "One-click selection commands that isolate the main subject (or delete the background), used before replacing a background generatively."),
    ("Neural Filters", "A panel of AI-powered filters (Skin Smoothing, Smart Portrait, Colorize, Style Transfer, Landscape Mixer and more) driven by simple sliders, each output on its own layer."),
    ("Portrait retouching", "Cleaning and enhancing a photo of a person — skin, stray hair, distractions, eyes or expression — quickly and non-destructively while keeping them natural."),
    ("Layer mask", "A black-and-white attachment to a layer that hides or reveals part of it as you paint, used to blend a generative layer precisely into the scene."),
    ("Blend mode", "A setting that changes how a layer's pixels combine with those below (Multiply, Screen, Overlay, Soft Light and others) to merge light, colour and texture."),
    ("Composite", "A finished image assembled from several layers — here, generative layers blended with masks and blend modes so it reads as one photograph."),
    ("Non-destructive editing", "Working so the original pixels are never overwritten — using generative layers, masks and adjustment layers — so every change stays reversible."),
    ("PSD", "Photoshop's native layered file format, which preserves generative layers, masks and blend modes so the deliverable stays fully editable."),
    ("Content Credentials", "Provenance metadata Firefly can attach to a result, recording that AI was used and how, to support transparent and responsible use."),
    ("Commercial use", "Using an image to promote or sell — which requires that Firefly's usage terms and the rights to every image, person and brand in it are all cleared."),
    ("Intellectual property (IP)", "The rights — copyright, trademark and likeness — that govern who may use an image, a design, a logo or a person's face, and that you must respect."),
]

# ------------------------------------------------------------------ version history
VERSION_HISTORY = [
    ("1.0", VERSION_DATE, "Initial release — C16 Generative AI for Adobe Photoshop courseware.", TRAINER),
]
