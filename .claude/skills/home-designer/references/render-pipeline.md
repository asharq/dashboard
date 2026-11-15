# Photoreal render pipeline (FAL)

- Model: `openai/gpt-image-2/edit`, `quality: "high"`, ~$0.21 per 1K image. Pilot proved faithful edits of our real photos beat "reframed" director's cuts.
- Use the **queue API** (sync fal.run times out at the 30 s proxy limit):
  `POST https://queue.fal.run/openai/gpt-image-2/edit` → `request_id`; poll `/requests/{id}/status` until COMPLETED; GET `/requests/{id}` → `images[0].url` (hosted on v3.fal.media / v3b.fal.media, allowed in the environment).
- Auth header is injected by the environment network secret; never send a key yourself.
- Inputs: `image_urls` as base64 data URIs. Image 1 = the real room photo (apply EXIF orientation first!). Extra images = reference cutouts/photos of items to add.
- Save results as artifact assets, then point the record at the asset id (`planos.*.render.img`, `settings.visions[]`).

## Prompt template (faithful edit)
"Edit image 1, a real photo of our {space}. Keep the room, furniture, walls, floor, lighting and camera angle exactly as they are. Clear the surface completely, then place only these objects, each matching its reference image exactly: 1. … 2. … Do not add any other objects, plants, books, text or decor. Photorealistic, same phone-camera look as the original."

## Prompt template (design vision)
Room-specific styling list + this direction: "Restoration Hardware–level warm modern, Thanksgiving week. Palette: oatmeal/warm-white walls as they are, taupe and cream textiles, walnut and oak, brushed brass, olive, one rust/terracotta accent. Warm 2700K lamplight. Calm, curated, no clutter; cords and electronics hidden. Keep the real architecture, floor, cabinets, windows, furniture positions and camera angle exactly; keep our real furniture recognizable. Photorealistic magazine photo of this exact apartment, not a 3D render."

## Known limits
Views through windows are invented. Small text (books, labels) may drift. Always label renders as AI previews.

## TV presentation
The app's Present mode (Today/Design → "Present on the TV", or open the app with #present) builds slides from `settings.visions` (room before/after), `settings.cabRenders` (cabinet interiors) and the 9-day path. Portrait photos are shown whole over a blurred fill for 16:9 screens.

## New angles without breaking the truth
For "new angle" hero shots, pass the approved after renders (not the raw photos) as the reference images and say: "SINGLE SOURCE OF TRUTH: every object, finish and color must match the references; only the camera moves." Works well for overheads, close vignettes and straight-on wides. For "every door open" shots, pass the room photo first, then each cabinet's after render.

## Where renders live in the app
`settings.visions` (room before/after), `settings.cabRenders` (every cabinet), `settings.storyRenders` (arrival-day story), `settings.heroRenders` (new angles + every-door-open). The TV presentation (Present on the TV) reads all four, and narrates with the `tts` capability.
