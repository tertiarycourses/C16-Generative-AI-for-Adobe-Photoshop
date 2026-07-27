"""
Domain 1 — Generative Editing Essentials in Photoshop. Labs 1-6.

THE CONNECTED PROJECT STARTS HERE, IN LAB 1.

Every lab in this course takes one connected deliverable — a brand campaign key
visual for the Solace Radiance Serum, a fictional botanical skincare product from
the studio Aster & Vale — one stage further. Lab 1 gets you oriented in
Photoshop's generative tools; Lab 2 builds a strong, reusable prompt; Lab 3 adds
and removes content with Generative Fill; Lab 4 extends the shot into a banner with
Generative Expand; Lab 5 cleans it up with the AI Remove tool; Lab 6 generates and
replaces the background. A reference pack and starter files are supplied; use your
own non-confidential product instead wherever you prefer.
"""

SCENARIO = (
 "Aster & Vale is a fictional botanical skincare studio launching a signature product: the Solace Radiance "
 "Serum — a small amber-glass dropper bottle with a matte cream label and a brushed-gold cap, sold as a calm, "
 "natural, premium product. The studio needs one campaign key visual of the serum that can be delivered three "
 "ways: a wide web banner, a square social post, and a lifestyle scene with a model. You are the brand "
 "designer, and across this course you take the Solace serum from a plain product photo all the way to a "
 "finished, layered campaign visual using only the generative AI built into Photoshop. Use this scenario only "
 "if you cannot use a real, non-confidential product of your own; your own product or brand is always welcome."
)

PROJECT_NOTE = (
 "BUILDING BLOCK — what you create in this lab becomes part of your Solace Radiance Serum campaign key "
 "visual, the connected project you assemble across all 10 labs."
)

DOMAIN1 = [
 dict(
 num=1, topic=1,
 title="Get Started with Firefly and Generative AI in Photoshop",
 objective="Set up Photoshop's generative tools, run your first Generative Fill, and learn the generate–review–refine loop and generative layers that every later lab uses.",
 desc="This lab gets you comfortable with the tools before any real campaign work begins. You confirm you are "
 "signed in to Adobe with Firefly credits, open the supplied Solace serum photo, and make a first selection so "
 "the Contextual Task Bar appears. You run a simple Generative Fill, see the three variations land on their own "
 "generative layer, and cycle through them in the Properties panel. You learn that the edit is non-destructive — "
 "the original photo is untouched — and where the generate, regenerate and variation controls live. By the end "
 "you understand the describe -> generate -> review -> refine loop that is the heart of generative AI in "
 "Photoshop. " + PROJECT_NOTE,
 build="A first Generative Fill applied to the Solace serum photo, with its three variations reviewed on a non-destructive generative layer — plus a clear understanding of the Contextual Task Bar and the generate–review–refine loop.",
 services="Adobe Photoshop, Adobe account / Firefly credits, the Contextual Task Bar, selection tools, Generative Fill, generative layers, the Properties panel variations",
 steps=[
 ("Create a project folder on your machine called 'Solace-campaign' so every file you make today stays together. Copy the supplied starter files (labs/starter-files/) into it, and open 'solace-serum.jpg' in Photoshop.", ""),
 ("Confirm you are ready to generate: check you are signed in to your Adobe account (top-right avatar) and that you have Firefly generative credits. Save the file straight away as a layered Photoshop file: File > Save As > 'solace-hero.psd'.", ""),
 ("Make your first selection so the generative tools appear: pick the Rectangular Marquee tool and drag a small empty area beside the bottle. The Contextual Task Bar floats up near the selection with a 'Generative Fill' button — this bar is your main way to work.", ""),
 ("Click Generative Fill, type a simple first prompt, and click Generate. Watch Photoshop return a result matched to the photo's light.",
  "a single small green eucalyptus sprig lying on the surface"),
 ("Look at what happened in the Layers panel: the result is on its own 'Generative Layer' above your photo — the original pixels are untouched. Hide and show that layer to prove the edit is non-destructive.", ""),
 ("Review the variations: with the generative layer selected, open the Properties panel and step through the three variations Firefly returned. Pick the one you like best; if none is right, click 'Generate' again for three more.", ""),
 ("Delete this warm-up generative layer (you were only learning the interface), so your 'solace-hero.psd' is back to the clean serum photo, ready for real work in the next labs.", ""),
 ("Write one line, in your own words, describing the loop you just used (select -> Generative Fill -> prompt -> review variations -> refine) and where the variations appear. You rely on this loop in every later lab.", ""),
 ],
 test="You have run a Generative Fill on the Solace serum photo, seen the three variations on a non-destructive generative layer, stepped through them in the Properties panel, and confirmed the original photo was untouched when you deleted the layer — proving you understand the generate–review–refine loop.",
 ),
 dict(
 num=2, topic=1,
 title="Write Effective Prompts for Image Generation",
 objective="Turn the supplied Solace reference pack into a strong, structured prompt that controls subject, style and detail, and save it as a reusable template.",
 desc="A good generative result starts with a good prompt, not a lucky one. In this lab you read the supplied "
 "Solace reference pack and shape it into a structured prompt with clear parts: the subject, a few descriptive "
 "details, a style, lighting, and what to avoid. Working on a spare area of the canvas, you test small prompt "
 "changes to feel how each one moves the result — describing what you WANT to see rather than giving an "
 "instruction — and you learn to keep prompts concise and iterate rather than over-load them. You save your best "
 "wording as a reusable template you will reuse across the rest of the campaign. " + PROJECT_NOTE,
 build="A structured Solace prompt (subject, details, style, lighting, negative) plus a reusable prompt template, saved in your project folder for use in Labs 3, 6 and 7.",
 services="Generative Fill prompt box, the supplied Solace prompt sheet and style notes, a structured prompt template, style and lighting keywords, negative wording",
 steps=[
 ("Open the supplied Solace reference pack (labs/reference-pack/): the prompt sheet and the style notes. Skim both so you know the product, its look, its colours and its mood before you write anything.", ""),
 ("In 'solace-hero.psd', select a spare area of the canvas to experiment in. Write a first prompt that names the subject and a couple of details only, and Generate.",
  "a few loose dried botanical leaves and small white flowers scattered on the surface"),
 ("Add a style and a lighting cue and regenerate. Notice how the look shifts while the subject stays the same — this shows how style and lighting steer the result independently of the subject.",
  "a few loose dried botanical leaves and small white flowers, soft natural daylight, calm minimalist premium skincare style, gentle shadows"),
 ("Describe what you WANT, not an instruction. Compare a 'wanted' prompt with an instruction-style one and see which behaves better, then keep the 'wanted' style.",
  "smooth softly-lit cream-coloured surface with subtle natural texture"),
 ("Add a short negative cue for what to avoid, and regenerate. Keep the whole prompt concise — a few clear phrases beat one long paragraph.",
  "soft natural daylight on a calm cream surface, minimalist premium skincare style — no text, no logos, no clutter, no harsh shadows"),
 ("Run one or two more single-change edits to feel how each word matters — for example swap 'soft natural daylight' for 'warm golden-hour light', or 'minimalist' for 'lush botanical' — and note which direction suits Solace.", ""),
 ("Combine your best choices into one clean prompt. Then check it against the prompting rule: does it name the subject, add a few details, set a style and lighting, and say what to avoid? Fill any gap.", ""),
 ("Save two things in your Solace-campaign folder: your final Solace prompt, and a reusable template version with clearly marked slots — [SUBJECT], [DETAILS], [STYLE], [LIGHTING], [NEGATIVE] — that you can reuse for any future product. Delete the experiment layers so the hero file stays clean.", ""),
 ],
 test="You have a structured Solace prompt that explicitly controls subject, style, detail and lighting plus a negative cue, you have confirmed that describing what you WANT works better than an instruction, and you have saved a reusable prompt template with clearly marked slots.",
 ),
 dict(
 num=3, topic=1,
 title="Add and Remove Content with Generative Fill",
 objective="Use Generative Fill to add supporting props to the serum photo and to remove a distracting object, all on non-destructive generative layers.",
 desc="Generative Fill does two opposite jobs from the same tool: adding content and removing it. In this lab you "
 "first add a supporting prop to the Solace hero shot — a sprig of botanicals or a soft prop beside the bottle — "
 "by selecting an empty area and describing what to insert, matched to the photo's light and perspective. You then "
 "remove an unwanted element — a stray object, a reflection or a bit of clutter — by selecting it and generating "
 "with an empty prompt, so Photoshop fills the gap with believable background. You work on generative layers "
 "throughout, refining the selection and re-generating until each edit is seamless. " + PROJECT_NOTE,
 build="A Solace hero shot with a supporting prop added and a distraction removed by Generative Fill, each on its own generative layer, blended so the edits are invisible.",
 services="Generative Fill (add and remove), selection tools, the Contextual Task Bar, generative layers, empty-prompt removal, variation review",
 steps=[
 ("Open 'solace-hero.psd' from Lab 2. Decide on one supporting prop that fits the brand — for example a small eucalyptus sprig or a couple of dried flowers resting near the bottle — using your style notes to keep it on-brand.", ""),
 ("Select the empty area where the prop should sit (Lasso or Rectangular Marquee), click Generative Fill, paste your prompt, and Generate. Keep the selection a sensible size — roughly where you want the object to appear.",
  "a small fresh eucalyptus sprig resting on the surface next to the bottle, soft natural daylight, gentle shadow, premium minimalist skincare style"),
 ("Review the three variations and pick the one whose light, scale and shadow best match the bottle. If the prop is too big, too bright or floating, adjust the selection or prompt and Generate again rather than accepting a weak result.", ""),
 ("Check the blend: zoom in on where the prop meets the surface and confirm the shadow direction and softness match the bottle's. If the edge looks pasted-on, re-generate or nudge the selection and try once more.", ""),
 ("Now remove a distraction. Find something you want gone — a stray speck, a dust mark, a reflection or a bit of background clutter — and select it snugly with the Lasso, leaving a small margin around it.", ""),
 ("Click Generative Fill, leave the prompt box EMPTY, and Generate. Photoshop removes the object and fills the gap with matching background. Review the variations and keep the cleanest fill.", ""),
 ("Rename your generative layers clearly ('prop - eucalyptus', 'remove - clutter') so the file stays organised for the composite later, and confirm each edit is still on its own layer above the untouched photo.", ""),
 ("Save 'solace-hero.psd'. You now have a cleaner, richer hero shot with one element added and one removed — both non-destructive and re-editable.", ""),
 ],
 test="Your Solace hero shot has a supporting prop added by Generative Fill whose light, scale and shadow match the bottle, and a distraction removed by an empty-prompt Generative Fill that left believable background — both on their own clearly named generative layers above the untouched photo.",
 ),
 dict(
 num=4, topic=1,
 title="Extend Images with Generative Expand",
 objective="Use Generative Expand to enlarge the canvas and re-frame the serum shot into a wide banner, letting Photoshop generate the new space to match.",
 desc="A square product shot is rarely the shape a campaign needs. In this lab you use Generative Expand to turn "
 "the Solace hero into a wide web banner. You select the Crop tool, drag the canvas out to a wide format, and let "
 "Photoshop generate the newly added space — matched to the existing scene — so the bottle sits comfortably off to "
 "one side with clean room for a headline. You also see how the same tool straightens a crooked shot and re-frames "
 "a subject. You keep the expansion on its own generative layer, review the variations, and refine the prompt so the "
 "new area is believable and leaves usable space. " + PROJECT_NOTE,
 build="A wide banner version of the Solace hero created with Generative Expand, with the new canvas space generated to match the scene and clear room reserved for a headline — kept non-destructive on a generative layer.",
 services="Generative Expand, the Crop tool, canvas resizing, aspect-ratio presets, Generative Fill prompt for expansion, variation review",
 steps=[
 ("Open 'solace-hero.psd' from Lab 3. Save a copy as 'solace-banner.psd' so you keep the square hero intact and work the wide format separately.", ""),
 ("Select the Crop tool. In the options bar, set a wide ratio (for example 16:9 or a custom wide banner) so you can drag the canvas out horizontally rather than cropping in.", ""),
 ("Drag the crop handles outward to the left and right so the bottle ends up off-centre (say, on the right third) with plenty of empty canvas on the other side for a headline. The added area shows as blank canvas.", ""),
 ("Before committing, make sure Generative Expand is enabled (the Contextual Task Bar / options show a Generative Expand or Fill option). You can add a short prompt to guide the new space, or leave it empty to simply continue the scene.",
  "continue the same calm cream surface and soft natural daylight, empty and uncluttered, room for text"),
 ("Commit the crop. Photoshop generates the new canvas area on a generative layer and returns variations. Review them and keep the one where the new surface blends seamlessly with the original and the light is consistent.", ""),
 ("Check the seams: zoom along the joins between the original photo and the generated area and confirm there is no visible line, colour shift or repeated pattern. If there is, re-generate or expand in two smaller steps instead of one big one.", ""),
 ("Try the tool's other uses briefly on a duplicate: straighten a slightly rotated version (rotate, then Generative Expand fills the exposed corners) so you understand how it fixes crooked shots and re-frames subjects.", ""),
 ("Save 'solace-banner.psd'. You now have a wide, well-composed banner with generated space that reads as part of the original photo and leaves clean room for a headline.", ""),
 ],
 test="You have expanded the Solace hero into a wide banner with Generative Expand, the generated canvas space blends seamlessly with the original photo (consistent light, no visible seam or repeat), the bottle is composed off to one side, and clear space is reserved for a headline — all kept non-destructive.",
 ),
 dict(
 num=5, topic=1,
 title="One-Click Cleanup with the AI Remove Tool",
 objective="Use the AI Remove tool to erase small distractions and blemishes from the serum images in single strokes, and know when it beats Generative Fill.",
 desc="Not every cleanup needs a full selection. In this lab you use Photoshop's brush-based Remove tool for fast, "
 "one-stroke tidy-ups on the Solace images — a dust speck, a fingerprint on the glass, a scratch on the label, a "
 "distracting highlight or a small stray object. You brush over the distraction and Photoshop erases it and "
 "reconstructs what should be behind it, no marquee required. You learn to size the brush to the mark, work in small "
 "passes for a clean result, and judge when the Remove tool is quicker than a Generative Fill and when a full "
 "selection is the better choice. All edits stay non-destructive on their own layer. " + PROJECT_NOTE,
 build="Clean Solace hero and banner images with small distractions and blemishes removed in single strokes by the AI Remove tool, reconstructed believably and kept on a non-destructive layer.",
 services="The Remove tool (AI Remove), adjustable brush size, one-stroke removal and reconstruction, 'Sample all layers' option, a new blank layer for non-destructive edits",
 steps=[
 ("Open 'solace-hero.psd' from Lab 4 (or the banner). Add a new blank layer above the photo and, in the Remove tool options, enable 'Sample all layers' so your cleanups stay on that layer and the original is untouched.", ""),
 ("Select the Remove tool from the toolbar (grouped with the Spot Healing / retouch tools). Set a brush size just a little larger than the blemish you want gone — the tool works best sized to the mark, not the whole area.", ""),
 ("Find a small distraction on the glass or label — a dust speck, a fingerprint smudge or a tiny scratch — and brush a single stroke over it. Release, and Photoshop erases it and rebuilds the surface behind it.", ""),
 ("If the result isn't perfect, undo and try again with a slightly larger brush or a second short stroke. Small, deliberate passes give a cleaner reconstruction than one big scrub.", ""),
 ("Clean a distracting highlight or a stray object in the background the same way. For anything larger or more complex, note that a Generative Fill with a selection (Lab 3) gives you more control — use the right tool for the size of the job.", ""),
 ("Move to 'solace-banner.psd' and run the same quick cleanup across the wider frame, checking the generated-expansion area from Lab 4 for any small artefacts and removing them.", ""),
 ("Zoom to 100% and scan the whole image edge to edge, removing any last specks so the product reads as flawless and premium.", ""),
 ("Save both files. Your hero and banner are now clean and blemish-free, with every cleanup kept on its own non-destructive layer.", ""),
 ],
 test="You have removed small distractions and blemishes from the Solace hero and banner with single strokes of the AI Remove tool, the areas behind them are reconstructed believably, you can explain when the Remove tool beats a Generative Fill, and all cleanups sit on a non-destructive layer above the untouched photo.",
 ),
 dict(
 num=6, topic=1,
 title="Generate and Replace the Background",
 objective="Isolate the serum and use Generative Fill to replace its background with a completely new, described scene whose light and perspective match the bottle.",
 desc="Replacing a background is where generative editing really changes the look of a shot. In this lab you isolate "
 "the Solace bottle with a one-click Select Subject, invert the selection to target everything behind it, and use "
 "Generative Fill to describe a brand-new backdrop — a soft botanical setting, a calm stone ledge, or a gradient "
 "studio scene — that Photoshop generates to match the bottle's lighting and perspective. You refine the subject "
 "selection so edges look natural, review the variations, and re-generate until the product sits believably in its "
 "new world. The new background lands on its own generative layer, so the bottle and its scene stay separate and "
 "editable. " + PROJECT_NOTE,
 build="A Solace hero shot placed into a completely new, described background generated to match the bottle's light and perspective, with a clean subject edge and the background kept on its own generative layer.",
 services="Select Subject, Select > Inverse, Select and Mask / refine edge, Generative Fill for backgrounds, the reusable prompt from Lab 2, variation review",
 steps=[
 ("Open 'solace-hero.psd' from Lab 5. Select the layer with the bottle and choose Select > Subject (or the Contextual Task Bar's 'Select Subject') to isolate the serum in one click.", ""),
 ("Refine the selection so the edge is clean: use Select and Mask to smooth and slightly feather the edge, especially around the dropper cap and the glass, so the bottle won't look cut out against the new scene.", ""),
 ("Invert the selection (Select > Inverse) so everything EXCEPT the bottle is now selected — this is the area you will replace.", ""),
 ("Click Generative Fill and describe the new background, reusing and adapting your Solace prompt from Lab 2. Generate.",
  "a calm minimalist background of soft botanical shadows on a warm cream wall, gentle natural daylight from the left, shallow depth of field, premium skincare style"),
 ("Review the three variations and choose the one whose light direction and warmth match the bottle. If the background light fights the product (shadows on the wrong side), regenerate with the light direction stated explicitly.", ""),
 ("Check that the bottle sits in the scene, not on top of it: confirm the ground shadow and the background depth feel consistent. Add a small contact shadow with a low Generative Fill selection or a soft brush if the bottle looks like it is floating.", ""),
 ("Generate one alternative background for the client to choose from (for example a stone-ledge scene) on a second generative layer, and keep both hidden / shown so you can compare — a real deliverable often offers options.",
  "a smooth pale stone ledge with a soft out-of-focus green garden behind, warm natural daylight from the left, calm premium skincare style"),
 ("Save 'solace-hero.psd'. Your serum now sits in a completely new, coherent scene, with the background on its own generative layer and the bottle preserved and editable.", ""),
 ],
 test="You have isolated the Solace bottle with a clean, refined edge and replaced its background using Generative Fill with a described scene whose light direction and perspective match the bottle, the product sits believably in the scene (consistent contact shadow), and the new background is on its own generative layer with an alternative option kept alongside.",
 ),
]
