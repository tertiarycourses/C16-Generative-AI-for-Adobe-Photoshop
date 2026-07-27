# Lab 3 — Add and Remove Content with Generative Fill

**Topic 01:** Generative Editing Essentials in Photoshop  |  **Day 1**  |  **Approx. 40 min**  |  **Course:** Generative AI for Adobe Photoshop (C16)

## Scenario

Aster & Vale is a fictional botanical skincare studio launching a signature product: the Solace Radiance Serum — a small amber-glass dropper bottle with a matte cream label and a brushed-gold cap, sold as a calm, natural, premium product. The studio needs one campaign key visual of the serum that can be delivered three ways: a wide web banner, a square social post, and a lifestyle scene with a model. You are the brand designer, and across this course you take the Solace serum from a plain product photo all the way to a finished, layered campaign visual using only the generative AI built into Photoshop. Use this scenario only if you cannot use a real, non-confidential product of your own; your own product or brand is always welcome.

## Goal

Use Generative Fill to add supporting props to the serum photo and to remove a distracting object, all on non-destructive generative layers.

## What you'll build

A Solace hero shot with a supporting prop added and a distraction removed by Generative Fill, each on its own generative layer, blended so the edits are invisible.

**Tools and techniques:** Generative Fill (add and remove), selection tools, the Contextual Task Bar, generative layers, empty-prompt removal, variation review

## Prerequisites

- Completed Lab 2 (you have a strong Solace prompt and template).
- 'solace-hero.psd' open with the clean serum photo.

## Steps

### Step 1

Open 'solace-hero.psd' from Lab 2. Decide on one supporting prop that fits the brand — for example a small eucalyptus sprig or a couple of dried flowers resting near the bottle — using your style notes to keep it on-brand.

### Step 2

Select the empty area where the prop should sit (Lasso or Rectangular Marquee), click Generative Fill, paste your prompt, and Generate. Keep the selection a sensible size — roughly where you want the object to appear.

Text to use (paste into Photoshop's Generative Fill / generate box):

```text
a small fresh eucalyptus sprig resting on the surface next to the bottle, soft natural daylight, gentle shadow, premium minimalist skincare style
```

### Step 3

Review the three variations and pick the one whose light, scale and shadow best match the bottle. If the prop is too big, too bright or floating, adjust the selection or prompt and Generate again rather than accepting a weak result.

### Step 4

Check the blend: zoom in on where the prop meets the surface and confirm the shadow direction and softness match the bottle's. If the edge looks pasted-on, re-generate or nudge the selection and try once more.

### Step 5

Now remove a distraction. Find something you want gone — a stray speck, a dust mark, a reflection or a bit of background clutter — and select it snugly with the Lasso, leaving a small margin around it.

### Step 6

Click Generative Fill, leave the prompt box EMPTY, and Generate. Photoshop removes the object and fills the gap with matching background. Review the variations and keep the cleanest fill.

### Step 7

Rename your generative layers clearly ('prop - eucalyptus', 'remove - clutter') so the file stays organised for the composite later, and confirm each edit is still on its own layer above the untouched photo.

### Step 8

Save 'solace-hero.psd'. You now have a cleaner, richer hero shot with one element added and one removed — both non-destructive and re-editable.

## Test it

Your Solace hero shot has a supporting prop added by Generative Fill whose light, scale and shadow match the bottle, and a distraction removed by an empty-prompt Generative Fill that left believable background — both on their own clearly named generative layers above the untouched photo.

## Troubleshooting

- **The added prop's light doesn't match.** State the light direction in the prompt ('soft daylight from the left, gentle shadow') and regenerate, or adjust the selection size.
- **The removed object leaves a smudge or ghost.** Re-select with a little more margin and generate again with an empty prompt; a snug but not tight selection fills cleanest.
- **The edit looks pasted-on at the edges.** Nudge the selection, regenerate, or add a layer mask and soften the join.

## Challenge

Add two different props on separate generative layers, then show/hide them to offer the client alternative compositions from one file.

## Reflection

LO3 — In your own words: Add and remove content non-destructively with Generative Fill and generative layers?

## Deliverable

Keep 'solace-hero.psd' with a prop added and a distraction removed on clearly named generative layers — the base for the expand and background labs.

---

*Generative AI for Adobe Photoshop (C16) · C16 · Version v1.0 · © 2026 Tertiary Infotech Academy Pte Ltd*
