# Generative AI for Adobe Photoshop (C16) — Learner Guide

**Course Code:** C16  |  **Conducted by:** Tertiary Infotech Academy Pte Ltd (UEN 201200696W)  |  **Version v1.0 · 27 July 2026**

## Contents

- [Introduction](#introduction)
- [Course Learning Outcomes](#course-learning-outcomes)
- [Before You Start — Preparation](#before-you-start--preparation)
- [Topic 01 — Generative Editing Essentials in Photoshop  (60%)](#topic-01--generative-editing-essentials-in-photoshop--60)
  - [Lab 1 — Get Started with Firefly and Generative AI in Photoshop](#lab-1--get-started-with-firefly-and-generative-ai-in-photoshop)
  - [Lab 2 — Write Effective Prompts for Image Generation](#lab-2--write-effective-prompts-for-image-generation)
  - [Lab 3 — Add and Remove Content with Generative Fill](#lab-3--add-and-remove-content-with-generative-fill)
  - [Lab 4 — Extend Images with Generative Expand](#lab-4--extend-images-with-generative-expand)
  - [Lab 5 — One-Click Cleanup with the AI Remove Tool](#lab-5--one-click-cleanup-with-the-ai-remove-tool)
  - [Lab 6 — Generate and Replace the Background](#lab-6--generate-and-replace-the-background)
- [Topic 02 — Advanced Generative Workflows  (40%)](#topic-02--advanced-generative-workflows--40)
  - [Lab 7 — Text-to-Image Generation with Reference Images and Styles](#lab-7--text-to-image-generation-with-reference-images-and-styles)
  - [Lab 8 — AI-Powered Portrait Retouching and Neural Filters](#lab-8--ai-powered-portrait-retouching-and-neural-filters)
  - [Lab 9 — Combine Generative Layers with Masks and Blend Modes](#lab-9--combine-generative-layers-with-masks-and-blend-modes)
  - [Lab 10 — Build the End-to-End Workflow and Check Commercial Use and IP](#lab-10--build-the-end-to-end-workflow-and-check-commercial-use-and-ip)
- [Wrap-Up](#wrap-up)
- [Next Steps](#next-steps)
- [Glossary](#glossary)


## Introduction

This Learner Guide accompanies the Generative AI for Adobe Photoshop (C16) course, conducted by Tertiary Infotech Academy Pte Ltd. It carries the full detail of all 10 hands-on labs, in the order you will run them, together with the concepts each lab depends on.

The labs build a single, connected deliverable — a brand campaign key visual for the Solace Radiance Serum, a fictional botanical skincare product from the studio Aster & Vale. You start in Lab 1 by getting oriented in Photoshop's generative tools, then in every lab you take the campaign one stage further — a strong prompt, added and removed content with Generative Fill, a Generative Expand banner, an AI Remove cleanup, a replaced background, a text-to-image lifestyle scene, an AI-retouched portrait, and finally a masked, blended composite you finish and check for commercial use. A reference pack and starter files are supplied; you may substitute your own non-confidential product wherever you prefer.


## Course Learning Outcomes

- LO1: Describe how generative AI (Adobe Firefly) works inside Photoshop and navigate the generate–review–refine loop using the Contextual Task Bar and generative layers.
- LO2: Write effective, structured prompts that control subject, style and detail for image generation in Photoshop.
- LO3: Add and remove content non-destructively with Generative Fill and generative layers.
- LO4: Extend an image beyond its original canvas with Generative Expand to re-compose and re-format it.
- LO5: Clean up an image in one click with the AI Remove tool to erase distractions and blemishes.
- LO6: Generate and replace a background to place a subject in a new, coherent scene.
- LO7: Generate images from text using reference images and styles to control the look of a result.
- LO8: Retouch portraits with AI — generative retouching and Neural Filters — naturally and ethically.
- LO9: Combine generative layers with masks and blend modes to composite a polished final image.
- LO10: Build an end-to-end generative design workflow and apply commercial-use and intellectual-property considerations to AI-generated visuals.


## Before You Start — Preparation

**What you need**

- A laptop (Windows or Mac) able to run the current release of Adobe Photoshop — a reasonably recent machine with 8 GB RAM minimum, 16 GB preferred.
- Adobe Photoshop installed and updated to a version with Generative Fill, Generative Expand and the Remove tool (a free trial is available from adobe.com). The trainer will confirm the version at the start of the day.
- An Adobe account signed in to Photoshop, with Firefly generative credits available — the labs stay within a modest number of generations, but check your credit balance before you start.
- An internet connection — the generative features process in the cloud, so they need to be online.
- The supplied Solace starter files and reference pack (a product photo, a portrait, a prompt sheet and style notes) — or a few photos and notes for your own non-confidential product to use instead.

**Verify your setup**

Before Lab 1, confirm Photoshop opens, that you can see the Contextual Task Bar with a 'Generative Fill' button when you make a selection, and that you are signed in to your Adobe account with credits available. If anything is missing, tell the trainer.

```bash
Open Photoshop  ·  make a selection and confirm the Contextual Task Bar shows Generative Fill  ·  check Firefly credits in your Adobe account
```

**Conventions used in every lab**

- Placeholders such as <YOUR PRODUCT> or <YOUR REFERENCE IMAGE> are replaced with your own values.
- Prompts to type into Photoshop's Generative Fill or generate box are shown in the 'Text to use' blocks — adapt them to your own product.
- Every lab ends with a 'Test it' step — an explicit check that the result meets the brief before you move on.
- Keep every file for one campaign in a single project folder, and save layered PSDs so your work stays non-destructive and editable.


## Topic 01 — Generative Editing Essentials in Photoshop  (60%)

Introduction to Adobe Firefly and generative AI in Photoshop · Writing effective prompts for image generation · Adding and removing content with Generative Fill · Extending images with Generative Expand · One-click cleanup with the AI Remove tool · Generating and replacing backgrounds

**Key concepts**

- Adobe Firefly and generative AI in Photoshop — Firefly is Adobe's image-generation model, built into Photoshop so you can add, remove, extend and reimagine parts of a photo by describing them in words, right on the canvas, without leaving the app.
- The Contextual Task Bar and the generate–review–refine loop — you make a selection, type a short prompt (or leave it blank), and Photoshop generates several variations; you review them, then regenerate or refine until one is right. This loop is the heart of every generative edit.
- Generative layers are non-destructive — every generative result lands on its own generative layer above your photo, so the original pixels are never touched; you can hide, re-generate, mask or delete a result at any time without harming the image underneath.
- Variations and generation credits — each generate produces three variations to choose from, and you can keep generating for more; generations use Firefly generative credits, so part of the craft is getting a strong result in fewer tries with a better selection and prompt.
- Writing effective prompts — a good prompt names the subject, adds a few descriptive details and, where it helps, a style; you describe what you WANT to see in the selected area (not an instruction like 'remove this'), keep it concise, and iterate rather than over-loading one prompt.
- Generative Fill to add and remove content — select an area and describe something to insert it seamlessly matched to the photo's light and perspective; select an object and generate with an empty prompt to remove it and fill the gap with a believable background.
- Generative Expand — enlarge the canvas with the Crop tool and Photoshop generates new image to fill the added space, so you can re-frame a subject, straighten a crooked shot, or reformat a square photo into a wide banner or a tall story, all in one step.
- The AI Remove tool — a brush-based one-click cleanup that erases distractions, blemishes, wires or stray objects and intelligently reconstructs what should be behind them, faster than a manual selection for small tidy-ups.
- Generating and replacing backgrounds — select the subject, invert the selection (or use Select Subject / Remove Background), then use Generative Fill to place the subject into a completely new, described scene whose lighting and perspective match the subject.


### Lab 1 — Get Started with Firefly and Generative AI in Photoshop

Learning outcome: Set up Photoshop's generative tools, run your first Generative Fill, and learn the generate–review–refine loop and generative layers that every later lab uses..

Goal: This lab gets you comfortable with the tools before any real campaign work begins. You confirm you are signed in to Adobe with Firefly credits, open the supplied Solace serum photo, and make a first selection so the Contextual Task Bar appears. You run a simple Generative Fill, see the three variations land on their own generative layer, and cycle through them in the Properties panel. You learn that the edit is non-destructive — the original photo is untouched — and where the generate, regenerate and variation controls live. By the end you understand the describe -> generate -> review -> refine loop that is the heart of generative AI in Photoshop. BUILDING BLOCK — what you create in this lab becomes part of your Solace Radiance Serum campaign key visual, the connected project you assemble across all 10 labs.

**What you'll build**

A first Generative Fill applied to the Solace serum photo, with its three variations reviewed on a non-destructive generative layer — plus a clear understanding of the Contextual Task Bar and the generate–review–refine loop.   (Tools: Adobe Photoshop, Adobe account / Firefly credits, the Contextual Task Bar, selection tools, Generative Fill, generative layers, the Properties panel variations.)

**Step-by-step**

1. Create a project folder on your machine called 'Solace-campaign' so every file you make today stays together. Copy the supplied starter files (labs/starter-files/) into it, and open 'solace-serum.jpg' in Photoshop.
2. Confirm you are ready to generate: check you are signed in to your Adobe account (top-right avatar) and that you have Firefly generative credits. Save the file straight away as a layered Photoshop file: File > Save As > 'solace-hero.psd'.
3. Make your first selection so the generative tools appear: pick the Rectangular Marquee tool and drag a small empty area beside the bottle. The Contextual Task Bar floats up near the selection with a 'Generative Fill' button — this bar is your main way to work.
4. Click Generative Fill, type a simple first prompt, and click Generate. Watch Photoshop return a result matched to the photo's light.

   ```bash
   a single small green eucalyptus sprig lying on the surface
   ```

5. Look at what happened in the Layers panel: the result is on its own 'Generative Layer' above your photo — the original pixels are untouched. Hide and show that layer to prove the edit is non-destructive.
6. Review the variations: with the generative layer selected, open the Properties panel and step through the three variations Firefly returned. Pick the one you like best; if none is right, click 'Generate' again for three more.
7. Delete this warm-up generative layer (you were only learning the interface), so your 'solace-hero.psd' is back to the clean serum photo, ready for real work in the next labs.
8. Write one line, in your own words, describing the loop you just used (select -> Generative Fill -> prompt -> review variations -> refine) and where the variations appear. You rely on this loop in every later lab.

**Test it**

You have run a Generative Fill on the Solace serum photo, seen the three variations on a non-destructive generative layer, stepped through them in the Properties panel, and confirmed the original photo was untouched when you deleted the layer — proving you understand the generate–review–refine loop.

> **Note:** Full commands and screenshots are in labs/lab-01-*.md. Use only images, people and brands you are authorised to use. Do not upload a real company's product photo, a copyrighted image, or a photo of a person without their consent, and check Adobe's current generative-AI usage terms before you publish or sell a result. Use the supplied Solace starter files rather than confidential material, and note that generative features process your images in the cloud under Adobe's terms of service.

---


### Lab 2 — Write Effective Prompts for Image Generation

Learning outcome: Turn the supplied Solace reference pack into a strong, structured prompt that controls subject, style and detail, and save it as a reusable template..

Goal: A good generative result starts with a good prompt, not a lucky one. In this lab you read the supplied Solace reference pack and shape it into a structured prompt with clear parts: the subject, a few descriptive details, a style, lighting, and what to avoid. Working on a spare area of the canvas, you test small prompt changes to feel how each one moves the result — describing what you WANT to see rather than giving an instruction — and you learn to keep prompts concise and iterate rather than over-load them. You save your best wording as a reusable template you will reuse across the rest of the campaign. BUILDING BLOCK — what you create in this lab becomes part of your Solace Radiance Serum campaign key visual, the connected project you assemble across all 10 labs.

**What you'll build**

A structured Solace prompt (subject, details, style, lighting, negative) plus a reusable prompt template, saved in your project folder for use in Labs 3, 6 and 7.   (Tools: Generative Fill prompt box, the supplied Solace prompt sheet and style notes, a structured prompt template, style and lighting keywords, negative wording.)

**Step-by-step**

1. Open the supplied Solace reference pack (labs/reference-pack/): the prompt sheet and the style notes. Skim both so you know the product, its look, its colours and its mood before you write anything.
2. In 'solace-hero.psd', select a spare area of the canvas to experiment in. Write a first prompt that names the subject and a couple of details only, and Generate.

   ```bash
   a few loose dried botanical leaves and small white flowers scattered on the surface
   ```

3. Add a style and a lighting cue and regenerate. Notice how the look shifts while the subject stays the same — this shows how style and lighting steer the result independently of the subject.

   ```bash
   a few loose dried botanical leaves and small white flowers, soft natural daylight, calm minimalist premium skincare style, gentle shadows
   ```

4. Describe what you WANT, not an instruction. Compare a 'wanted' prompt with an instruction-style one and see which behaves better, then keep the 'wanted' style.

   ```bash
   smooth softly-lit cream-coloured surface with subtle natural texture
   ```

5. Add a short negative cue for what to avoid, and regenerate. Keep the whole prompt concise — a few clear phrases beat one long paragraph.

   ```bash
   soft natural daylight on a calm cream surface, minimalist premium skincare style — no text, no logos, no clutter, no harsh shadows
   ```

6. Run one or two more single-change edits to feel how each word matters — for example swap 'soft natural daylight' for 'warm golden-hour light', or 'minimalist' for 'lush botanical' — and note which direction suits Solace.
7. Combine your best choices into one clean prompt. Then check it against the prompting rule: does it name the subject, add a few details, set a style and lighting, and say what to avoid? Fill any gap.
8. Save two things in your Solace-campaign folder: your final Solace prompt, and a reusable template version with clearly marked slots — [SUBJECT], [DETAILS], [STYLE], [LIGHTING], [NEGATIVE] — that you can reuse for any future product. Delete the experiment layers so the hero file stays clean.

**Test it**

You have a structured Solace prompt that explicitly controls subject, style, detail and lighting plus a negative cue, you have confirmed that describing what you WANT works better than an instruction, and you have saved a reusable prompt template with clearly marked slots.

> **Note:** Full commands and screenshots are in labs/lab-02-*.md. Use only images, people and brands you are authorised to use. Do not upload a real company's product photo, a copyrighted image, or a photo of a person without their consent, and check Adobe's current generative-AI usage terms before you publish or sell a result. Use the supplied Solace starter files rather than confidential material, and note that generative features process your images in the cloud under Adobe's terms of service.

---


### Lab 3 — Add and Remove Content with Generative Fill

Learning outcome: Use Generative Fill to add supporting props to the serum photo and to remove a distracting object, all on non-destructive generative layers..

Goal: Generative Fill does two opposite jobs from the same tool: adding content and removing it. In this lab you first add a supporting prop to the Solace hero shot — a sprig of botanicals or a soft prop beside the bottle — by selecting an empty area and describing what to insert, matched to the photo's light and perspective. You then remove an unwanted element — a stray object, a reflection or a bit of clutter — by selecting it and generating with an empty prompt, so Photoshop fills the gap with believable background. You work on generative layers throughout, refining the selection and re-generating until each edit is seamless. BUILDING BLOCK — what you create in this lab becomes part of your Solace Radiance Serum campaign key visual, the connected project you assemble across all 10 labs.

**What you'll build**

A Solace hero shot with a supporting prop added and a distraction removed by Generative Fill, each on its own generative layer, blended so the edits are invisible.   (Tools: Generative Fill (add and remove), selection tools, the Contextual Task Bar, generative layers, empty-prompt removal, variation review.)

**Step-by-step**

1. Open 'solace-hero.psd' from Lab 2. Decide on one supporting prop that fits the brand — for example a small eucalyptus sprig or a couple of dried flowers resting near the bottle — using your style notes to keep it on-brand.
2. Select the empty area where the prop should sit (Lasso or Rectangular Marquee), click Generative Fill, paste your prompt, and Generate. Keep the selection a sensible size — roughly where you want the object to appear.

   ```bash
   a small fresh eucalyptus sprig resting on the surface next to the bottle, soft natural daylight, gentle shadow, premium minimalist skincare style
   ```

3. Review the three variations and pick the one whose light, scale and shadow best match the bottle. If the prop is too big, too bright or floating, adjust the selection or prompt and Generate again rather than accepting a weak result.
4. Check the blend: zoom in on where the prop meets the surface and confirm the shadow direction and softness match the bottle's. If the edge looks pasted-on, re-generate or nudge the selection and try once more.
5. Now remove a distraction. Find something you want gone — a stray speck, a dust mark, a reflection or a bit of background clutter — and select it snugly with the Lasso, leaving a small margin around it.
6. Click Generative Fill, leave the prompt box EMPTY, and Generate. Photoshop removes the object and fills the gap with matching background. Review the variations and keep the cleanest fill.
7. Rename your generative layers clearly ('prop - eucalyptus', 'remove - clutter') so the file stays organised for the composite later, and confirm each edit is still on its own layer above the untouched photo.
8. Save 'solace-hero.psd'. You now have a cleaner, richer hero shot with one element added and one removed — both non-destructive and re-editable.

**Test it**

Your Solace hero shot has a supporting prop added by Generative Fill whose light, scale and shadow match the bottle, and a distraction removed by an empty-prompt Generative Fill that left believable background — both on their own clearly named generative layers above the untouched photo.

> **Note:** Full commands and screenshots are in labs/lab-03-*.md. Use only images, people and brands you are authorised to use. Do not upload a real company's product photo, a copyrighted image, or a photo of a person without their consent, and check Adobe's current generative-AI usage terms before you publish or sell a result. Use the supplied Solace starter files rather than confidential material, and note that generative features process your images in the cloud under Adobe's terms of service.

---


### Lab 4 — Extend Images with Generative Expand

Learning outcome: Use Generative Expand to enlarge the canvas and re-frame the serum shot into a wide banner, letting Photoshop generate the new space to match..

Goal: A square product shot is rarely the shape a campaign needs. In this lab you use Generative Expand to turn the Solace hero into a wide web banner. You select the Crop tool, drag the canvas out to a wide format, and let Photoshop generate the newly added space — matched to the existing scene — so the bottle sits comfortably off to one side with clean room for a headline. You also see how the same tool straightens a crooked shot and re-frames a subject. You keep the expansion on its own generative layer, review the variations, and refine the prompt so the new area is believable and leaves usable space. BUILDING BLOCK — what you create in this lab becomes part of your Solace Radiance Serum campaign key visual, the connected project you assemble across all 10 labs.

**What you'll build**

A wide banner version of the Solace hero created with Generative Expand, with the new canvas space generated to match the scene and clear room reserved for a headline — kept non-destructive on a generative layer.   (Tools: Generative Expand, the Crop tool, canvas resizing, aspect-ratio presets, Generative Fill prompt for expansion, variation review.)

**Step-by-step**

1. Open 'solace-hero.psd' from Lab 3. Save a copy as 'solace-banner.psd' so you keep the square hero intact and work the wide format separately.
2. Select the Crop tool. In the options bar, set a wide ratio (for example 16:9 or a custom wide banner) so you can drag the canvas out horizontally rather than cropping in.
3. Drag the crop handles outward to the left and right so the bottle ends up off-centre (say, on the right third) with plenty of empty canvas on the other side for a headline. The added area shows as blank canvas.
4. Before committing, make sure Generative Expand is enabled (the Contextual Task Bar / options show a Generative Expand or Fill option). You can add a short prompt to guide the new space, or leave it empty to simply continue the scene.

   ```bash
   continue the same calm cream surface and soft natural daylight, empty and uncluttered, room for text
   ```

5. Commit the crop. Photoshop generates the new canvas area on a generative layer and returns variations. Review them and keep the one where the new surface blends seamlessly with the original and the light is consistent.
6. Check the seams: zoom along the joins between the original photo and the generated area and confirm there is no visible line, colour shift or repeated pattern. If there is, re-generate or expand in two smaller steps instead of one big one.
7. Try the tool's other uses briefly on a duplicate: straighten a slightly rotated version (rotate, then Generative Expand fills the exposed corners) so you understand how it fixes crooked shots and re-frames subjects.
8. Save 'solace-banner.psd'. You now have a wide, well-composed banner with generated space that reads as part of the original photo and leaves clean room for a headline.

**Test it**

You have expanded the Solace hero into a wide banner with Generative Expand, the generated canvas space blends seamlessly with the original photo (consistent light, no visible seam or repeat), the bottle is composed off to one side, and clear space is reserved for a headline — all kept non-destructive.

> **Note:** Full commands and screenshots are in labs/lab-04-*.md. Use only images, people and brands you are authorised to use. Do not upload a real company's product photo, a copyrighted image, or a photo of a person without their consent, and check Adobe's current generative-AI usage terms before you publish or sell a result. Use the supplied Solace starter files rather than confidential material, and note that generative features process your images in the cloud under Adobe's terms of service.

---


### Lab 5 — One-Click Cleanup with the AI Remove Tool

Learning outcome: Use the AI Remove tool to erase small distractions and blemishes from the serum images in single strokes, and know when it beats Generative Fill..

Goal: Not every cleanup needs a full selection. In this lab you use Photoshop's brush-based Remove tool for fast, one-stroke tidy-ups on the Solace images — a dust speck, a fingerprint on the glass, a scratch on the label, a distracting highlight or a small stray object. You brush over the distraction and Photoshop erases it and reconstructs what should be behind it, no marquee required. You learn to size the brush to the mark, work in small passes for a clean result, and judge when the Remove tool is quicker than a Generative Fill and when a full selection is the better choice. All edits stay non-destructive on their own layer. BUILDING BLOCK — what you create in this lab becomes part of your Solace Radiance Serum campaign key visual, the connected project you assemble across all 10 labs.

**What you'll build**

Clean Solace hero and banner images with small distractions and blemishes removed in single strokes by the AI Remove tool, reconstructed believably and kept on a non-destructive layer.   (Tools: The Remove tool (AI Remove), adjustable brush size, one-stroke removal and reconstruction, 'Sample all layers' option, a new blank layer for non-destructive edits.)

**Step-by-step**

1. Open 'solace-hero.psd' from Lab 4 (or the banner). Add a new blank layer above the photo and, in the Remove tool options, enable 'Sample all layers' so your cleanups stay on that layer and the original is untouched.
2. Select the Remove tool from the toolbar (grouped with the Spot Healing / retouch tools). Set a brush size just a little larger than the blemish you want gone — the tool works best sized to the mark, not the whole area.
3. Find a small distraction on the glass or label — a dust speck, a fingerprint smudge or a tiny scratch — and brush a single stroke over it. Release, and Photoshop erases it and rebuilds the surface behind it.
4. If the result isn't perfect, undo and try again with a slightly larger brush or a second short stroke. Small, deliberate passes give a cleaner reconstruction than one big scrub.
5. Clean a distracting highlight or a stray object in the background the same way. For anything larger or more complex, note that a Generative Fill with a selection (Lab 3) gives you more control — use the right tool for the size of the job.
6. Move to 'solace-banner.psd' and run the same quick cleanup across the wider frame, checking the generated-expansion area from Lab 4 for any small artefacts and removing them.
7. Zoom to 100% and scan the whole image edge to edge, removing any last specks so the product reads as flawless and premium.
8. Save both files. Your hero and banner are now clean and blemish-free, with every cleanup kept on its own non-destructive layer.

**Test it**

You have removed small distractions and blemishes from the Solace hero and banner with single strokes of the AI Remove tool, the areas behind them are reconstructed believably, you can explain when the Remove tool beats a Generative Fill, and all cleanups sit on a non-destructive layer above the untouched photo.

> **Note:** Full commands and screenshots are in labs/lab-05-*.md. Use only images, people and brands you are authorised to use. Do not upload a real company's product photo, a copyrighted image, or a photo of a person without their consent, and check Adobe's current generative-AI usage terms before you publish or sell a result. Use the supplied Solace starter files rather than confidential material, and note that generative features process your images in the cloud under Adobe's terms of service.

---


### Lab 6 — Generate and Replace the Background

Learning outcome: Isolate the serum and use Generative Fill to replace its background with a completely new, described scene whose light and perspective match the bottle..

Goal: Replacing a background is where generative editing really changes the look of a shot. In this lab you isolate the Solace bottle with a one-click Select Subject, invert the selection to target everything behind it, and use Generative Fill to describe a brand-new backdrop — a soft botanical setting, a calm stone ledge, or a gradient studio scene — that Photoshop generates to match the bottle's lighting and perspective. You refine the subject selection so edges look natural, review the variations, and re-generate until the product sits believably in its new world. The new background lands on its own generative layer, so the bottle and its scene stay separate and editable. BUILDING BLOCK — what you create in this lab becomes part of your Solace Radiance Serum campaign key visual, the connected project you assemble across all 10 labs.

**What you'll build**

A Solace hero shot placed into a completely new, described background generated to match the bottle's light and perspective, with a clean subject edge and the background kept on its own generative layer.   (Tools: Select Subject, Select > Inverse, Select and Mask / refine edge, Generative Fill for backgrounds, the reusable prompt from Lab 2, variation review.)

**Step-by-step**

1. Open 'solace-hero.psd' from Lab 5. Select the layer with the bottle and choose Select > Subject (or the Contextual Task Bar's 'Select Subject') to isolate the serum in one click.
2. Refine the selection so the edge is clean: use Select and Mask to smooth and slightly feather the edge, especially around the dropper cap and the glass, so the bottle won't look cut out against the new scene.
3. Invert the selection (Select > Inverse) so everything EXCEPT the bottle is now selected — this is the area you will replace.
4. Click Generative Fill and describe the new background, reusing and adapting your Solace prompt from Lab 2. Generate.

   ```bash
   a calm minimalist background of soft botanical shadows on a warm cream wall, gentle natural daylight from the left, shallow depth of field, premium skincare style
   ```

5. Review the three variations and choose the one whose light direction and warmth match the bottle. If the background light fights the product (shadows on the wrong side), regenerate with the light direction stated explicitly.
6. Check that the bottle sits in the scene, not on top of it: confirm the ground shadow and the background depth feel consistent. Add a small contact shadow with a low Generative Fill selection or a soft brush if the bottle looks like it is floating.
7. Generate one alternative background for the client to choose from (for example a stone-ledge scene) on a second generative layer, and keep both hidden / shown so you can compare — a real deliverable often offers options.

   ```bash
   a smooth pale stone ledge with a soft out-of-focus green garden behind, warm natural daylight from the left, calm premium skincare style
   ```

8. Save 'solace-hero.psd'. Your serum now sits in a completely new, coherent scene, with the background on its own generative layer and the bottle preserved and editable.

**Test it**

You have isolated the Solace bottle with a clean, refined edge and replaced its background using Generative Fill with a described scene whose light direction and perspective match the bottle, the product sits believably in the scene (consistent contact shadow), and the new background is on its own generative layer with an alternative option kept alongside.

> **Note:** Full commands and screenshots are in labs/lab-06-*.md. Use only images, people and brands you are authorised to use. Do not upload a real company's product photo, a copyrighted image, or a photo of a person without their consent, and check Adobe's current generative-AI usage terms before you publish or sell a result. Use the supplied Solace starter files rather than confidential material, and note that generative features process your images in the cloud under Adobe's terms of service.

---


## Topic 02 — Advanced Generative Workflows  (40%)

Text-to-image generation with reference images and styles · AI-powered portrait retouching and Neural Filters · Combining generative layers with masks and blend modes · Building end-to-end generative design workflows · Commercial use and intellectual-property considerations

**Key concepts**

- Text-to-image generation — beyond editing an existing photo, you can generate a brand-new image from a text prompt (in Photoshop's generate workflow or in the Firefly web app) to create concepts, backgrounds and lifestyle scenes from nothing but a description.
- Reference images and style controls — you steer a generated image's look by supplying a reference image (to match composition or subject) and by choosing a style, content type (photo vs art), effects, colour and lighting, so results stay on-brand instead of random.
- AI-powered portrait retouching — generative retouching and the Remove/Fill tools clean skin, remove flyaway hair and stray objects and even adjust eyes or expression on a portrait, quickly and non-destructively, while keeping the person looking natural.
- Neural Filters — a panel of AI-powered filters (Skin Smoothing, Smart Portrait, Colorize, Style Transfer, Landscape Mixer and more) that apply sophisticated, model-driven edits from simple sliders, each output kept on its own layer.
- Masks with generative layers — a layer mask hides or reveals part of a generative layer with black-and-white painting, so you blend a generated element precisely into the scene and control exactly where it shows.
- Blend modes — a blend mode changes how a generative layer's pixels combine with the layers below (Multiply, Screen, Overlay, Soft Light and others), letting you merge light, shadow, colour and texture so a composite reads as one photograph.
- End-to-end generative design workflow — real work chains these tools together: generate or edit the subject, expand and re-frame, replace the background, retouch, then composite generative layers with masks and blend modes into one finished, layered deliverable you can revise.
- Commercial use and licensing — Firefly is designed to be commercially safe (trained on licensed and public-domain content), but you must still check Adobe's current generative-AI usage terms, any credit limits, and the rights to every non-Firefly image, model or brand you bring in.
- Intellectual property and responsible use — you own your prompts and your edits, but you must respect other people's copyright, trademarks and likeness; disclose AI use where required, avoid deceptive edits, and note that Firefly can attach Content Credentials (provenance metadata) to a result.


### Lab 7 — Text-to-Image Generation with Reference Images and Styles

Learning outcome: Generate a brand-new lifestyle scene for the campaign from a text prompt, steering the look with a reference image and Firefly's style controls..

Goal: Editing an existing photo is only half of generative AI; you can also create a whole new image from nothing but a description. In this lab you use text-to-image — in Photoshop's generate workflow or the Firefly web app — to produce a lifestyle scene for the Solace campaign (a calm bathroom shelf, a spa-like setting, a botanical flat-lay). You steer the result with your Lab 2 prompt, a reference image to guide composition and subject, and Firefly's style controls — content type (photo vs art), a visual style, effects, colour and lighting — so the scene stays on-brand rather than random. You generate several options and bring the best into your project. BUILDING BLOCK — what you create in this lab becomes part of your Solace Radiance Serum campaign key visual, the connected project you assemble across all 10 labs.

**What you'll build**

A text-to-image lifestyle scene for the Solace campaign, generated from your prompt and steered by a reference image and Firefly style controls, brought into the project as a new layer.   (Tools: Text-to-image (Photoshop generate / Firefly web app), reference image / composition guide, style and content-type controls, effects, colour and lighting settings, generate and download.)

**Step-by-step**

1. Open the reference pack's style notes and your reusable prompt from Lab 2. Decide on the lifestyle scene you want for the campaign — for example a calm bathroom shelf, a spa setting, or a botanical flat-lay that suits the serum.
2. Start a text-to-image generation (in Photoshop's generate box, or at the Firefly web app). Enter a scene prompt based on your Solace prompt and Generate a first set.

   ```bash
   a calm spa-like bathroom shelf with soft towels, eucalyptus and a warm cream wall, soft natural daylight from the left, minimalist premium skincare lifestyle scene, empty space on the right for a product
   ```

3. Add a reference image to steer composition or subject: upload the supplied reference (or your own authorised image) so the result follows a layout you want, and regenerate. Compare how much the reference changes the output.
4. Set the style controls: choose the Photo content type (not Art), pick a matching visual style, and adjust colour and lighting so the scene reads warm, calm and premium. Regenerate and watch the mood shift with the settings.
5. Generate several variations and shortlist two or three scenes that suit Solace and leave clear space for the product. Keep the light direction consistent with your hero bottle (light from the left) so they will composite together later.
6. Bring your chosen scene into the project: place it into your Solace PSD as a new layer (File > Place Embedded, or copy from the Firefly result), naming the layer 'lifestyle-scene'. Keep it non-destructive.
7. Note the provenance: if you used the Firefly web app, keep the downloaded file and its Content Credentials, and record which reference image and style settings produced the scene, so the result is documented for the IP check in Lab 10.
8. Save your PSD. You now have an on-brand, AI-generated lifestyle scene, controlled by a reference image and style settings, ready to host the product in the composite.

**Test it**

You have generated an on-brand lifestyle scene for the Solace campaign with text-to-image, demonstrably steered it with a reference image and Firefly's style, colour and lighting controls, chosen a scene with space for the product and consistent light direction, and placed it into your project as a named, non-destructive layer.

> **Note:** Full commands and screenshots are in labs/lab-07-*.md. Use only images, people and brands you are authorised to use. Do not upload a real company's product photo, a copyrighted image, or a photo of a person without their consent, and check Adobe's current generative-AI usage terms before you publish or sell a result. Use the supplied Solace starter files rather than confidential material, and note that generative features process your images in the cloud under Adobe's terms of service.

---


### Lab 8 — AI-Powered Portrait Retouching and Neural Filters

Learning outcome: Retouch the supplied model portrait with AI — generative retouching, the Remove tool and Neural Filters — naturally and ethically, keeping every edit non-destructive..

Goal: A campaign often features a person, and AI makes portrait retouching fast — but it must stay natural and ethical. In this lab you retouch the supplied Solace model portrait (a person holding or applying the serum). You clean skin and remove distractions with generative retouching and the Remove tool, then use Neural Filters — Skin Smoothing for gentle, believable skin, and optionally Smart Portrait or Colorize — driven by simple sliders, each output kept on its own layer. You retouch with restraint so the person still looks like themselves, and you note the consent and likeness responsibilities that come with editing a real face. BUILDING BLOCK — what you create in this lab becomes part of your Solace Radiance Serum campaign key visual, the connected project you assemble across all 10 labs.

**What you'll build**

A naturally retouched Solace model portrait: clean skin and removed distractions via generative retouching and the Remove tool, plus a subtle Neural Filters pass — all non-destructive and kept believable.   (Tools: Generative retouching, the Remove tool, Neural Filters (Skin Smoothing, Smart Portrait, Colorize), sliders, per-filter output layers, non-destructive retouching.)

**Step-by-step**

1. Open the supplied 'solace-model.jpg' portrait (or your own photo of a person who has consented to being edited). Save it as 'solace-model.psd' and duplicate the background layer so the original stays intact.
2. Remove obvious distractions first: use the Remove tool (Lab 5) to brush away flyaway hairs, a stray blemish, or a distracting object in the background, on a new layer with 'Sample all layers' on.
3. Clean any larger issue with generative retouching: select a distraction (a logo on clothing, an object) and use Generative Fill with an empty prompt to remove it, or describe a clean replacement, keeping it on its own layer.
4. Open Filters > Neural Filters and enable Skin Smoothing. Use the Blur and Smoothness sliders with restraint — aim for healthy, even skin that still shows natural texture, not a plastic look. Output it to a new layer.
5. Optionally try Smart Portrait or Colorize on a duplicate to see what they do (adjust gaze, expression, or colourise) — but for a premium skincare brand, keep the final look subtle and realistic. Discard any edit that looks artificial.
6. Judge the retouch honestly: toggle the before/after and confirm the person still looks like themselves. Over-smoothed skin or altered features undermine both trust and the brand — dial edits back until they read as natural.
7. Record the ethics: note that this is a real (or fictional-consented) person, that you have the right to edit and use their image, and that you have not made deceptive changes to their body or identity — you will include this in the IP check in Lab 10.
8. Save 'solace-model.psd'. You have a clean, naturally retouched portrait on non-destructive layers, ready to composite into the campaign.

**Test it**

You have retouched the Solace model portrait with the Remove tool, generative retouching and a subtle Skin Smoothing Neural Filter, every edit is on its own non-destructive layer, the person still looks natural and like themselves, and you have recorded the consent and likeness responsibilities for the portrait.

> **Note:** Full commands and screenshots are in labs/lab-08-*.md. Use only images, people and brands you are authorised to use. Do not upload a real company's product photo, a copyrighted image, or a photo of a person without their consent, and check Adobe's current generative-AI usage terms before you publish or sell a result. Use the supplied Solace starter files rather than confidential material, and note that generative features process your images in the cloud under Adobe's terms of service.

---


### Lab 9 — Combine Generative Layers with Masks and Blend Modes

Learning outcome: Composite the product, background, lifestyle scene and portrait into one image using layer masks and blend modes so it reads as a single photograph..

Goal: This is where the pieces become one campaign visual. In this lab you assemble the generative layers you have built — the clean hero bottle, its background or lifestyle scene, supporting props, and elements from the retouched portrait — into a single composite. You use layer masks to blend each element in precisely, painting black to hide and white to reveal, so edges disappear. You use blend modes — Multiply for shadows, Screen or Overlay for light and glow, Soft Light for tone — to merge light, colour and texture so nothing looks pasted on. You match colour and add contact shadows so the whole image reads as one photograph. BUILDING BLOCK — what you create in this lab becomes part of your Solace Radiance Serum campaign key visual, the connected project you assemble across all 10 labs.

**What you'll build**

A single composited Solace key visual assembling the product, background/lifestyle scene and supporting elements, blended with layer masks and blend modes and colour-matched so it reads as one photograph.   (Tools: Layer masks, brush painting on masks, blend modes (Multiply, Screen, Overlay, Soft Light), grouping and ordering layers, adjustment layers for colour matching, contact shadows.)

**Step-by-step**

1. Open your Solace PSD and bring the pieces together in one document: the hero bottle, the chosen background or lifestyle scene, your props, and any element from the retouched portrait. Order the layers back-to-front (scene at the bottom, product on top).
2. Add a layer mask to the product layer and paint with a soft black brush to hide its old edge/background so it sits cleanly on the new scene. Paint white to bring back anything you hid by mistake — masks are fully reversible.
3. Blend a shadow with a blend mode: put the bottle's contact shadow on its own layer and set it to Multiply so it darkens the surface beneath naturally instead of covering it with grey.
4. Add glow or highlight where light hits the glass or a botanical: on a new layer set to Screen or Overlay, paint a soft warm light, then lower the opacity so it reads as real light, not a sticker.
5. Match colour across the composite: add a Curves or Color Balance adjustment layer (clipped where needed) so the product, scene and portrait element share the same warmth and contrast — mismatched colour is what breaks a composite.
6. Refine every seam: zoom in and tidy each mask edge with a small soft brush, and use a Soft Light layer to unify texture and tone across the join between generated and photographed areas.
7. Group the finished layers ('PRODUCT', 'SCENE', 'LIGHT', 'COLOR') so the file is tidy and a client revision is easy. Toggle groups on and off to confirm each contributes and nothing is redundant.
8. Save the layered PSD. Step back and check the whole image reads as one photograph — consistent light direction, matched colour, believable shadows — with no element looking pasted on.

**Test it**

You have composited the Solace product, background/scene and supporting elements into one image using layer masks (painting black/white to blend) and blend modes (Multiply for shadow, Screen/Overlay for light, Soft Light for tone), colour-matched with an adjustment layer, and the result reads as a single photograph with consistent light and believable shadows.

> **Note:** Full commands and screenshots are in labs/lab-09-*.md. Use only images, people and brands you are authorised to use. Do not upload a real company's product photo, a copyrighted image, or a photo of a person without their consent, and check Adobe's current generative-AI usage terms before you publish or sell a result. Use the supplied Solace starter files rather than confidential material, and note that generative features process your images in the cloud under Adobe's terms of service.

---


### Lab 10 — Build the End-to-End Workflow and Check Commercial Use and IP

Learning outcome: Finish the campaign key visual as one end-to-end layered file, export it in the formats a campaign needs, and run the commercial-use and intellectual-property checks that govern real work..

Goal: The final lab turns your work into a real deliverable and makes it safe to ship. You review the whole end-to-end workflow — prompt, fill, expand, remove, background, text-to-image, retouch, composite — as one connected chain, tidy the layered file, and add the campaign headline space you reserved. You export the key visual in the formats a campaign needs (a wide banner, a square social post and a tall story), reusing Generative Expand to reformat. Then you run the commercial-use and IP check: Adobe's current generative-AI usage terms, credit limits, the rights to every non-Firefly image, person and brand, Content Credentials, and honest disclosure — so the visual is fit to publish. BUILDING BLOCK — what you create in this lab becomes part of your Solace Radiance Serum campaign key visual, the connected project you assemble across all 10 labs.

**What you'll build**

A finished, exported Solace campaign key visual in three formats from one end-to-end layered PSD, accompanied by a completed commercial-use and IP checklist covering usage terms, rights, Content Credentials and disclosure.   (Tools: Layered PSD finishing, Generative Expand for reformatting, Export As / Save a Copy (PNG/JPG), Content Credentials, Adobe generative-AI usage terms, an IP and rights checklist.)

**Step-by-step**

1. Open your composited Solace PSD from Lab 9. Walk the layer stack top to bottom and confirm the end-to-end chain is all there and non-destructive: prompt-driven fills, the expand, the cleanups, the background, the lifestyle scene, the retouch, and the blended composite.
2. Finish the key visual: add the headline space you reserved earlier (leave room for text rather than baking in final copy), tidy layer names and groups, and flatten a COPY only — never your master PSD — for export.
3. Export the primary wide banner: File > Export > Export As (or Save a Copy) to a high-quality JPG/PNG at the banner size. Keep the layered master PSD untouched alongside it.
4. Reformat for other placements with Generative Expand (Lab 4): from the master, produce a square social post and a tall story by expanding/recomposing the canvas and re-exporting each — one visual, three formats.
5. Turn on Content Credentials for your exports (Firefly/Photoshop's Content Credentials option) so the files carry provenance metadata recording that generative AI was used — a mark of responsible, transparent work.
6. Run the commercial-use check: confirm the generated content came from Firefly (designed for commercial safety), review Adobe's CURRENT generative-AI usage terms and your generative-credit limits, and confirm nothing blocks using the visual to promote the product.
7. Run the IP and rights check against a short checklist: every non-Firefly image is one you own or are licensed to use; the model gave consent for this use of their likeness; no third-party logo, artwork or trademark appears without permission; and you have made no deceptive edit. Note where AI use should be disclosed.
8. Save everything into your Solace-campaign folder — the layered master PSD, the three exported formats and the completed IP checklist. This is your finished, publishable deliverable, built end to end and cleared for use.

**Test it**

You have finished the Solace campaign key visual as one end-to-end, non-destructive layered PSD, exported it in three campaign formats using Generative Expand to reformat, attached Content Credentials, and completed a commercial-use and IP checklist (Adobe usage terms and credits, rights to every image/person/brand, consent, no deceptive edits, disclosure) — so the visual is fit to publish.

> **Note:** Full commands and screenshots are in labs/lab-10-*.md. Use only images, people and brands you are authorised to use. Do not upload a real company's product photo, a copyrighted image, or a photo of a person without their consent, and check Adobe's current generative-AI usage terms before you publish or sell a result. Use the supplied Solace starter files rather than confidential material, and note that generative features process your images in the cloud under Adobe's terms of service.

---


## Wrap-Up

You have taken one hero product — the Solace Radiance Serum — through the entire generative-AI workflow in Photoshop in a single day, from a plain product photo and a clear prompt to a finished, layered brand campaign key visual, and checked it for commercial use and IP.

**What you built**

- A strong, reusable prompt that controls subject, style and detail for generative edits and image generation.
- A clean hero shot with content added and removed by Generative Fill and a one-click AI Remove cleanup.
- A wide banner produced with Generative Expand, and a completely replaced, coherent background.
- A text-to-image lifestyle scene steered by a reference image and style controls, and an AI-retouched portrait.
- A masked, blended composite assembled into one end-to-end layered campaign key visual, checked for commercial use and IP.

**What to do next**

- Rebuild the campaign for a real, non-confidential product of your own using the same prompt template and workflow.
- Export the key visual in the formats a real campaign needs — a wide web banner, a square social post and a tall story — reusing your Generative Expand skills.
- Keep your prompt sheet and layered PSD as reusable templates so future visuals follow the same clean, non-destructive workflow.
- Always check Adobe's generative-AI usage terms and the rights to every image, person and brand, and disclose AI assistance where appropriate before you publish or sell.

---


## Next Steps

- First pass: complete every lab yourself, following the steps and verifying each 'Test it' check.
- Second pass: rebuild the key visual from your prompt and starter photo alone, compositing it without the step-by-step.
- Apply the workflow to a real, non-confidential product or brand of your own.
- Review each lab's detailed steps in this guide and re-create the campaign in your own Photoshop.


## Glossary

- **Generative AI** — AI that creates new content — here, images — from a text prompt or an existing image, rather than only filtering pixels that already exist.
- **Adobe Firefly** — Adobe's generative image model, built into Photoshop, that powers Generative Fill, Generative Expand, background generation and text-to-image.
- **Generative Fill** — A Photoshop feature that generates content into a selected area from a text prompt — to add an object, or (with an empty prompt) to remove one and fill the gap.
- **Generative Expand** — Enlarging the canvas with the Crop tool so Photoshop generates new image to fill the added space, used to re-frame, straighten or reformat a photo.
- **Generative layer** — The special layer each generative result lands on, keeping the edit non-destructive and separately editable, re-generatable and maskable.
- **Contextual Task Bar** — The floating bar that appears near your selection offering the right next action — such as Generative Fill — so you work directly on the canvas.
- **Variations** — The set of results (three at a time) Photoshop returns for each generation, shown in the Properties panel so you can pick the best or generate more.
- **Generative credits** — Firefly's usage allowance; each generation consumes credits, so a good selection and prompt that get a result in fewer tries are part of the craft.
- **Prompt** — The text you type to describe what you want generated; describe what you WANT to see in the area, concisely, and iterate rather than over-loading one prompt.
- **Reference image** — An image you supply to steer a text-to-image result toward a particular composition, subject or look, instead of relying on words alone.
- **Style / content type** — Firefly controls that set whether a result is a photo or art and apply a visual style, effects, colour and lighting to keep it on-brand.
- **Remove tool (AI Remove)** — A brush-based Photoshop tool that erases a distraction or blemish in a stroke and reconstructs what should be behind it.
- **Select Subject / Remove Background** — One-click selection commands that isolate the main subject (or delete the background), used before replacing a background generatively.
- **Neural Filters** — A panel of AI-powered filters (Skin Smoothing, Smart Portrait, Colorize, Style Transfer, Landscape Mixer and more) driven by simple sliders, each output on its own layer.
- **Portrait retouching** — Cleaning and enhancing a photo of a person — skin, stray hair, distractions, eyes or expression — quickly and non-destructively while keeping them natural.
- **Layer mask** — A black-and-white attachment to a layer that hides or reveals part of it as you paint, used to blend a generative layer precisely into the scene.
- **Blend mode** — A setting that changes how a layer's pixels combine with those below (Multiply, Screen, Overlay, Soft Light and others) to merge light, colour and texture.
- **Composite** — A finished image assembled from several layers — here, generative layers blended with masks and blend modes so it reads as one photograph.
- **Non-destructive editing** — Working so the original pixels are never overwritten — using generative layers, masks and adjustment layers — so every change stays reversible.
- **PSD** — Photoshop's native layered file format, which preserves generative layers, masks and blend modes so the deliverable stays fully editable.
- **Content Credentials** — Provenance metadata Firefly can attach to a result, recording that AI was used and how, to support transparent and responsible use.
- **Commercial use** — Using an image to promote or sell — which requires that Firefly's usage terms and the rights to every image, person and brand in it are all cleared.
- **Intellectual property (IP)** — The rights — copyright, trademark and likeness — that govern who may use an image, a design, a logo or a person's face, and that you must respect.
