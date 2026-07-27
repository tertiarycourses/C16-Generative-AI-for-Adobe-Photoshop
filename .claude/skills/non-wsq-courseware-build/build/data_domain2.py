"""
Domain 2 — Advanced Generative Workflows. Labs 7-10.

THE CONNECTED PROJECT CONTINUES — the same Solace Radiance Serum campaign.

Lab 7 generates a lifestyle scene from text using a reference image and style
controls; Lab 8 retouches a model portrait with AI retouching and Neural Filters;
Lab 9 composites the generative layers with masks and blend modes into one image;
Lab 10 builds the end-to-end workflow into a finished, exported key visual and
applies the commercial-use and intellectual-property checks that govern real work.
Use your own product and images instead of Solace wherever you prefer.
"""

PROJECT_NOTE = (
 "BUILDING BLOCK — what you create in this lab becomes part of your Solace Radiance Serum campaign key "
 "visual, the connected project you assemble across all 10 labs."
)

DOMAIN2 = [
 dict(
 num=7, topic=2,
 title="Text-to-Image Generation with Reference Images and Styles",
 objective="Generate a brand-new lifestyle scene for the campaign from a text prompt, steering the look with a reference image and Firefly's style controls.",
 desc="Editing an existing photo is only half of generative AI; you can also create a whole new image from nothing "
 "but a description. In this lab you use text-to-image — in Photoshop's generate workflow or the Firefly web app — "
 "to produce a lifestyle scene for the Solace campaign (a calm bathroom shelf, a spa-like setting, a botanical "
 "flat-lay). You steer the result with your Lab 2 prompt, a reference image to guide composition and subject, and "
 "Firefly's style controls — content type (photo vs art), a visual style, effects, colour and lighting — so the "
 "scene stays on-brand rather than random. You generate several options and bring the best into your project. " + PROJECT_NOTE,
 build="A text-to-image lifestyle scene for the Solace campaign, generated from your prompt and steered by a reference image and Firefly style controls, brought into the project as a new layer.",
 services="Text-to-image (Photoshop generate / Firefly web app), reference image / composition guide, style and content-type controls, effects, colour and lighting settings, generate and download",
 steps=[
 ("Open the reference pack's style notes and your reusable prompt from Lab 2. Decide on the lifestyle scene you want for the campaign — for example a calm bathroom shelf, a spa setting, or a botanical flat-lay that suits the serum.", ""),
 ("Start a text-to-image generation (in Photoshop's generate box, or at the Firefly web app). Enter a scene prompt based on your Solace prompt and Generate a first set.",
  "a calm spa-like bathroom shelf with soft towels, eucalyptus and a warm cream wall, soft natural daylight from the left, minimalist premium skincare lifestyle scene, empty space on the right for a product"),
 ("Add a reference image to steer composition or subject: upload the supplied reference (or your own authorised image) so the result follows a layout you want, and regenerate. Compare how much the reference changes the output.", ""),
 ("Set the style controls: choose the Photo content type (not Art), pick a matching visual style, and adjust colour and lighting so the scene reads warm, calm and premium. Regenerate and watch the mood shift with the settings.", ""),
 ("Generate several variations and shortlist two or three scenes that suit Solace and leave clear space for the product. Keep the light direction consistent with your hero bottle (light from the left) so they will composite together later.", ""),
 ("Bring your chosen scene into the project: place it into your Solace PSD as a new layer (File > Place Embedded, or copy from the Firefly result), naming the layer 'lifestyle-scene'. Keep it non-destructive.", ""),
 ("Note the provenance: if you used the Firefly web app, keep the downloaded file and its Content Credentials, and record which reference image and style settings produced the scene, so the result is documented for the IP check in Lab 10.", ""),
 ("Save your PSD. You now have an on-brand, AI-generated lifestyle scene, controlled by a reference image and style settings, ready to host the product in the composite.", ""),
 ],
 test="You have generated an on-brand lifestyle scene for the Solace campaign with text-to-image, demonstrably steered it with a reference image and Firefly's style, colour and lighting controls, chosen a scene with space for the product and consistent light direction, and placed it into your project as a named, non-destructive layer.",
 ),
 dict(
 num=8, topic=2,
 title="AI-Powered Portrait Retouching and Neural Filters",
 objective="Retouch the supplied model portrait with AI — generative retouching, the Remove tool and Neural Filters — naturally and ethically, keeping every edit non-destructive.",
 desc="A campaign often features a person, and AI makes portrait retouching fast — but it must stay natural and "
 "ethical. In this lab you retouch the supplied Solace model portrait (a person holding or applying the serum). "
 "You clean skin and remove distractions with generative retouching and the Remove tool, then use Neural Filters — "
 "Skin Smoothing for gentle, believable skin, and optionally Smart Portrait or Colorize — driven by simple sliders, "
 "each output kept on its own layer. You retouch with restraint so the person still looks like themselves, and you "
 "note the consent and likeness responsibilities that come with editing a real face. " + PROJECT_NOTE,
 build="A naturally retouched Solace model portrait: clean skin and removed distractions via generative retouching and the Remove tool, plus a subtle Neural Filters pass — all non-destructive and kept believable.",
 services="Generative retouching, the Remove tool, Neural Filters (Skin Smoothing, Smart Portrait, Colorize), sliders, per-filter output layers, non-destructive retouching",
 steps=[
 ("Open the supplied 'solace-model.jpg' portrait (or your own photo of a person who has consented to being edited). Save it as 'solace-model.psd' and duplicate the background layer so the original stays intact.", ""),
 ("Remove obvious distractions first: use the Remove tool (Lab 5) to brush away flyaway hairs, a stray blemish, or a distracting object in the background, on a new layer with 'Sample all layers' on.", ""),
 ("Clean any larger issue with generative retouching: select a distraction (a logo on clothing, an object) and use Generative Fill with an empty prompt to remove it, or describe a clean replacement, keeping it on its own layer.", ""),
 ("Open Filters > Neural Filters and enable Skin Smoothing. Use the Blur and Smoothness sliders with restraint — aim for healthy, even skin that still shows natural texture, not a plastic look. Output it to a new layer.", ""),
 ("Optionally try Smart Portrait or Colorize on a duplicate to see what they do (adjust gaze, expression, or colourise) — but for a premium skincare brand, keep the final look subtle and realistic. Discard any edit that looks artificial.", ""),
 ("Judge the retouch honestly: toggle the before/after and confirm the person still looks like themselves. Over-smoothed skin or altered features undermine both trust and the brand — dial edits back until they read as natural.", ""),
 ("Record the ethics: note that this is a real (or fictional-consented) person, that you have the right to edit and use their image, and that you have not made deceptive changes to their body or identity — you will include this in the IP check in Lab 10.", ""),
 ("Save 'solace-model.psd'. You have a clean, naturally retouched portrait on non-destructive layers, ready to composite into the campaign.", ""),
 ],
 test="You have retouched the Solace model portrait with the Remove tool, generative retouching and a subtle Skin Smoothing Neural Filter, every edit is on its own non-destructive layer, the person still looks natural and like themselves, and you have recorded the consent and likeness responsibilities for the portrait.",
 ),
 dict(
 num=9, topic=2,
 title="Combine Generative Layers with Masks and Blend Modes",
 objective="Composite the product, background, lifestyle scene and portrait into one image using layer masks and blend modes so it reads as a single photograph.",
 desc="This is where the pieces become one campaign visual. In this lab you assemble the generative layers you have "
 "built — the clean hero bottle, its background or lifestyle scene, supporting props, and elements from the retouched "
 "portrait — into a single composite. You use layer masks to blend each element in precisely, painting black to hide "
 "and white to reveal, so edges disappear. You use blend modes — Multiply for shadows, Screen or Overlay for light "
 "and glow, Soft Light for tone — to merge light, colour and texture so nothing looks pasted on. You match colour and "
 "add contact shadows so the whole image reads as one photograph. " + PROJECT_NOTE,
 build="A single composited Solace key visual assembling the product, background/lifestyle scene and supporting elements, blended with layer masks and blend modes and colour-matched so it reads as one photograph.",
 services="Layer masks, brush painting on masks, blend modes (Multiply, Screen, Overlay, Soft Light), grouping and ordering layers, adjustment layers for colour matching, contact shadows",
 steps=[
 ("Open your Solace PSD and bring the pieces together in one document: the hero bottle, the chosen background or lifestyle scene, your props, and any element from the retouched portrait. Order the layers back-to-front (scene at the bottom, product on top).", ""),
 ("Add a layer mask to the product layer and paint with a soft black brush to hide its old edge/background so it sits cleanly on the new scene. Paint white to bring back anything you hid by mistake — masks are fully reversible.", ""),
 ("Blend a shadow with a blend mode: put the bottle's contact shadow on its own layer and set it to Multiply so it darkens the surface beneath naturally instead of covering it with grey.", ""),
 ("Add glow or highlight where light hits the glass or a botanical: on a new layer set to Screen or Overlay, paint a soft warm light, then lower the opacity so it reads as real light, not a sticker.", ""),
 ("Match colour across the composite: add a Curves or Color Balance adjustment layer (clipped where needed) so the product, scene and portrait element share the same warmth and contrast — mismatched colour is what breaks a composite.", ""),
 ("Refine every seam: zoom in and tidy each mask edge with a small soft brush, and use a Soft Light layer to unify texture and tone across the join between generated and photographed areas.", ""),
 ("Group the finished layers ('PRODUCT', 'SCENE', 'LIGHT', 'COLOR') so the file is tidy and a client revision is easy. Toggle groups on and off to confirm each contributes and nothing is redundant.", ""),
 ("Save the layered PSD. Step back and check the whole image reads as one photograph — consistent light direction, matched colour, believable shadows — with no element looking pasted on.", ""),
 ],
 test="You have composited the Solace product, background/scene and supporting elements into one image using layer masks (painting black/white to blend) and blend modes (Multiply for shadow, Screen/Overlay for light, Soft Light for tone), colour-matched with an adjustment layer, and the result reads as a single photograph with consistent light and believable shadows.",
 ),
 dict(
 num=10, topic=2,
 title="Build the End-to-End Workflow and Check Commercial Use and IP",
 objective="Finish the campaign key visual as one end-to-end layered file, export it in the formats a campaign needs, and run the commercial-use and intellectual-property checks that govern real work.",
 desc="The final lab turns your work into a real deliverable and makes it safe to ship. You review the whole "
 "end-to-end workflow — prompt, fill, expand, remove, background, text-to-image, retouch, composite — as one "
 "connected chain, tidy the layered file, and add the campaign headline space you reserved. You export the key visual "
 "in the formats a campaign needs (a wide banner, a square social post and a tall story), reusing Generative Expand "
 "to reformat. Then you run the commercial-use and IP check: Adobe's current generative-AI usage terms, credit "
 "limits, the rights to every non-Firefly image, person and brand, Content Credentials, and honest disclosure — so "
 "the visual is fit to publish. " + PROJECT_NOTE,
 build="A finished, exported Solace campaign key visual in three formats from one end-to-end layered PSD, accompanied by a completed commercial-use and IP checklist covering usage terms, rights, Content Credentials and disclosure.",
 services="Layered PSD finishing, Generative Expand for reformatting, Export As / Save a Copy (PNG/JPG), Content Credentials, Adobe generative-AI usage terms, an IP and rights checklist",
 steps=[
 ("Open your composited Solace PSD from Lab 9. Walk the layer stack top to bottom and confirm the end-to-end chain is all there and non-destructive: prompt-driven fills, the expand, the cleanups, the background, the lifestyle scene, the retouch, and the blended composite.", ""),
 ("Finish the key visual: add the headline space you reserved earlier (leave room for text rather than baking in final copy), tidy layer names and groups, and flatten a COPY only — never your master PSD — for export.", ""),
 ("Export the primary wide banner: File > Export > Export As (or Save a Copy) to a high-quality JPG/PNG at the banner size. Keep the layered master PSD untouched alongside it.", ""),
 ("Reformat for other placements with Generative Expand (Lab 4): from the master, produce a square social post and a tall story by expanding/recomposing the canvas and re-exporting each — one visual, three formats.", ""),
 ("Turn on Content Credentials for your exports (Firefly/Photoshop's Content Credentials option) so the files carry provenance metadata recording that generative AI was used — a mark of responsible, transparent work.", ""),
 ("Run the commercial-use check: confirm the generated content came from Firefly (designed for commercial safety), review Adobe's CURRENT generative-AI usage terms and your generative-credit limits, and confirm nothing blocks using the visual to promote the product.", ""),
 ("Run the IP and rights check against a short checklist: every non-Firefly image is one you own or are licensed to use; the model gave consent for this use of their likeness; no third-party logo, artwork or trademark appears without permission; and you have made no deceptive edit. Note where AI use should be disclosed.", ""),
 ("Save everything into your Solace-campaign folder — the layered master PSD, the three exported formats and the completed IP checklist. This is your finished, publishable deliverable, built end to end and cleared for use.", ""),
 ],
 test="You have finished the Solace campaign key visual as one end-to-end, non-destructive layered PSD, exported it in three campaign formats using Generative Expand to reformat, attached Content Credentials, and completed a commercial-use and IP checklist (Adobe usage terms and credits, rights to every image/person/brand, consent, no deceptive edits, disclosure) — so the visual is fit to publish.",
 ),
]
