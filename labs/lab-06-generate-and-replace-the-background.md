# Lab 6 — Generate and Replace the Background

**Topic 01:** Generative Editing Essentials in Photoshop  |  **Day 1**  |  **Approx. 40 min**  |  **Course:** Generative AI for Adobe Photoshop (C16)

## Scenario

Aster & Vale is a fictional botanical skincare studio launching a signature product: the Solace Radiance Serum — a small amber-glass dropper bottle with a matte cream label and a brushed-gold cap, sold as a calm, natural, premium product. The studio needs one campaign key visual of the serum that can be delivered three ways: a wide web banner, a square social post, and a lifestyle scene with a model. You are the brand designer, and across this course you take the Solace serum from a plain product photo all the way to a finished, layered campaign visual using only the generative AI built into Photoshop. Use this scenario only if you cannot use a real, non-confidential product of your own; your own product or brand is always welcome.

## Goal

Isolate the serum and use Generative Fill to replace its background with a completely new, described scene whose light and perspective match the bottle.

## What you'll build

A Solace hero shot placed into a completely new, described background generated to match the bottle's light and perspective, with a clean subject edge and the background kept on its own generative layer.

**Tools and techniques:** Select Subject, Select > Inverse, Select and Mask / refine edge, Generative Fill for backgrounds, the reusable prompt from Lab 2, variation review

## Prerequisites

- Completed Lab 5 (clean hero and banner).
- Your reusable Solace prompt from Lab 2 for describing the new scene.

## Steps

### Step 1

Open 'solace-hero.psd' from Lab 5. Select the layer with the bottle and choose Select > Subject (or the Contextual Task Bar's 'Select Subject') to isolate the serum in one click.

### Step 2

Refine the selection so the edge is clean: use Select and Mask to smooth and slightly feather the edge, especially around the dropper cap and the glass, so the bottle won't look cut out against the new scene.

### Step 3

Invert the selection (Select > Inverse) so everything EXCEPT the bottle is now selected — this is the area you will replace.

### Step 4

Click Generative Fill and describe the new background, reusing and adapting your Solace prompt from Lab 2. Generate.

Text to use (paste into Photoshop's Generative Fill / generate box):

```text
a calm minimalist background of soft botanical shadows on a warm cream wall, gentle natural daylight from the left, shallow depth of field, premium skincare style
```

### Step 5

Review the three variations and choose the one whose light direction and warmth match the bottle. If the background light fights the product (shadows on the wrong side), regenerate with the light direction stated explicitly.

### Step 6

Check that the bottle sits in the scene, not on top of it: confirm the ground shadow and the background depth feel consistent. Add a small contact shadow with a low Generative Fill selection or a soft brush if the bottle looks like it is floating.

### Step 7

Generate one alternative background for the client to choose from (for example a stone-ledge scene) on a second generative layer, and keep both hidden / shown so you can compare — a real deliverable often offers options.

Text to use (paste into Photoshop's Generative Fill / generate box):

```text
a smooth pale stone ledge with a soft out-of-focus green garden behind, warm natural daylight from the left, calm premium skincare style
```

### Step 8

Save 'solace-hero.psd'. Your serum now sits in a completely new, coherent scene, with the background on its own generative layer and the bottle preserved and editable.

## Test it

You have isolated the Solace bottle with a clean, refined edge and replaced its background using Generative Fill with a described scene whose light direction and perspective match the bottle, the product sits believably in the scene (consistent contact shadow), and the new background is on its own generative layer with an alternative option kept alongside.

## Troubleshooting

- **The bottle looks cut out against the new background.** Refine the selection edge in Select and Mask (smooth, slightly feather), especially around the cap and glass.
- **The background light fights the product.** State the light direction explicitly ('daylight from the left') and regenerate so shadows fall the same way as on the bottle.
- **The product looks like it's floating.** Add a small contact shadow with a low Generative Fill selection or a soft brush on a Multiply layer.

## Challenge

Generate three different backgrounds (studio, botanical, stone ledge) on separate layers and present them as a mini set of options.

## Reflection

LO6 — In your own words: Generate and replace a background to place a subject in a new, coherent scene?

## Deliverable

Keep 'solace-hero.psd' with the serum in a new, coherent scene and an alternative background layer alongside — ready to composite.

---

*Generative AI for Adobe Photoshop (C16) · C16 · Version v1.0 · © 2026 Tertiary Infotech Academy Pte Ltd*
