# Lab 4 — Extend Images with Generative Expand

**Topic 01:** Generative Editing Essentials in Photoshop  |  **Day 1**  |  **Approx. 40 min**  |  **Course:** Generative AI for Adobe Photoshop (C16)

## Scenario

Aster & Vale is a fictional botanical skincare studio launching a signature product: the Solace Radiance Serum — a small amber-glass dropper bottle with a matte cream label and a brushed-gold cap, sold as a calm, natural, premium product. The studio needs one campaign key visual of the serum that can be delivered three ways: a wide web banner, a square social post, and a lifestyle scene with a model. You are the brand designer, and across this course you take the Solace serum from a plain product photo all the way to a finished, layered campaign visual using only the generative AI built into Photoshop. Use this scenario only if you cannot use a real, non-confidential product of your own; your own product or brand is always welcome.

## Goal

Use Generative Expand to enlarge the canvas and re-frame the serum shot into a wide banner, letting Photoshop generate the new space to match.

## What you'll build

A wide banner version of the Solace hero created with Generative Expand, with the new canvas space generated to match the scene and clear room reserved for a headline — kept non-destructive on a generative layer.

**Tools and techniques:** Generative Expand, the Crop tool, canvas resizing, aspect-ratio presets, Generative Fill prompt for expansion, variation review

## Prerequisites

- Completed Lab 3 (a cleaner hero shot with added/removed content).
- The Crop tool and Generative Expand available in your Photoshop version.

## Steps

### Step 1

Open 'solace-hero.psd' from Lab 3. Save a copy as 'solace-banner.psd' so you keep the square hero intact and work the wide format separately.

### Step 2

Select the Crop tool. In the options bar, set a wide ratio (for example 16:9 or a custom wide banner) so you can drag the canvas out horizontally rather than cropping in.

### Step 3

Drag the crop handles outward to the left and right so the bottle ends up off-centre (say, on the right third) with plenty of empty canvas on the other side for a headline. The added area shows as blank canvas.

### Step 4

Before committing, make sure Generative Expand is enabled (the Contextual Task Bar / options show a Generative Expand or Fill option). You can add a short prompt to guide the new space, or leave it empty to simply continue the scene.

Text to use (paste into Photoshop's Generative Fill / generate box):

```text
continue the same calm cream surface and soft natural daylight, empty and uncluttered, room for text
```

### Step 5

Commit the crop. Photoshop generates the new canvas area on a generative layer and returns variations. Review them and keep the one where the new surface blends seamlessly with the original and the light is consistent.

### Step 6

Check the seams: zoom along the joins between the original photo and the generated area and confirm there is no visible line, colour shift or repeated pattern. If there is, re-generate or expand in two smaller steps instead of one big one.

### Step 7

Try the tool's other uses briefly on a duplicate: straighten a slightly rotated version (rotate, then Generative Expand fills the exposed corners) so you understand how it fixes crooked shots and re-frames subjects.

### Step 8

Save 'solace-banner.psd'. You now have a wide, well-composed banner with generated space that reads as part of the original photo and leaves clean room for a headline.

## Test it

You have expanded the Solace hero into a wide banner with Generative Expand, the generated canvas space blends seamlessly with the original photo (consistent light, no visible seam or repeat), the bottle is composed off to one side, and clear space is reserved for a headline — all kept non-destructive.

## Troubleshooting

- **A visible seam or repeat appears in the new area.** Expand in two smaller steps instead of one big drag, and regenerate; state 'continue the same surface' in the prompt.
- **The generated space adds unwanted objects.** Add a short negative cue ('empty, uncluttered, room for text') or leave the prompt empty to simply continue the scene.
- **The bottle ends up centred with no room for a headline.** Re-crop so the bottle sits on one third and the empty canvas is on the other side.

## Challenge

Reformat the same hero into a tall story format (9:16) as well as the wide banner, proving one image can serve every placement.

## Reflection

LO4 — In your own words: Extend an image beyond its original canvas with Generative Expand to re-compose and re-format it?

## Deliverable

Keep 'solace-banner.psd' — a wide, well-composed banner with generated space and clear room for a headline.

---

*Generative AI for Adobe Photoshop (C16) · C16 · Version v1.0 · © 2026 Tertiary Infotech Academy Pte Ltd*
