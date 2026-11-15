# Design principles we use

## House rules (from Ashar + Huda, Nov 15)
- **Organizers:** natural bamboo in drawers and anything hidden (start with the big-utensil drawer D2); clear acrylic in upper cabinets (keep what we own); glass jars optional.
- **Fewer, bigger things.** Small knick-knacks stress us out. If a small object has no job, it leaves the room.
- **Palette:** beige/cream base, green from real plants, rust accents, one chocolate-brown throw. Nothing else.
- **Make the call.** Don't just restyle what's there: decide where each piece of furniture goes, what leaves the room, and what (little) to buy. Present it as a to-scale plan with numbered Keep / Move / Leaves / Buy decisions.

## Single source of truth (non-negotiable)
The Plan (`planos` in the app DB) lists, per surface, the exact catalog item IDs that go there. Every render, board, lookbook page and slideshow uses only those items, passed as reference images. Never invent decor or swap an object between shots. If a surface changes, change the Plan first, then re-render.

## Be bold, not conservative
Design as if anything can be removed. Start each surface from empty and ask: what is functional here, and what is the single most beautiful thing we own for it? Re-assign objects across rooms freely (a sculpture can leave the island for the console). Subtraction is the biggest lever; staging is the second.

## Styling
- Rule of three per surface: tall + medium + low, mixed textures. Odd numbers.
- Every surface gets fewer, bigger, deliberate pieces. Small figurines either group into one collection or leave.
- TV wall: two balanced groups at the ends, nothing in the middle; TV off reads as a dark frame.
- Glass tables: each lower shelf has one deliberate grouping or nothing; no cords visible through glass.
- One screen per surface. Tech, chargers, power strips hidden (cable boxes, velcro ties, drawer M3).
- Lighting: lamps on at 4pm, overheads off, 2700K bulbs everywhere.
- Thanksgiving accents only in the kitchen/island: pomegranates, clementines, small white pumpkins, eucalyptus.
- Sentimental anchors get their own stage: calligraphy (console), digital frame (right side table), Game Boy/iPhone frames (window corner).

## Kids 5 and 8
Knife block handles to the wall, chemicals locked (B4), meds top pantry shelf, magnets/small parts (levitating Cybertruck, Optimus, Pokémon cards) out of reach, candles lit only with an adult present, balcony locked. Give them a drawing station at their height (coffee table lower shelf).

## Everything has one home
| Category | Home |
|---|---|
| Keepsakes, photo strips, wedding items | Island drawer I3 |
| Papers, desk supplies | I2 |
| Junk drawer (tape, scissors kid-safe swap) | I1 |
| Tools, drill, cases | Laundry closet L1 top shelf |
| Cables, chargers, batteries | Media console M3 |
| Board games, cards | M4 |
| Gaming (PS5, controllers) | M2 (door cracked while on) |
| Glasses, mugs, coffee, tea, syrups | U8 above the coffee bar |
| Spices, Shan boxes | U3 |
| Snacks, baking | U4 / D3 |
| Medicine, vitamins | Pantry P1 top shelf |
| Cleaning, pods | Under-sink B4 (locked) |
| Plush, figurines, Pokémon cards | Pokémon room, one shelf |
| Kids' art supplies | Coffee table lower shelf basket |

## Step-by-step format
One room a day, ≤60 minutes, start at the front door and walk the sightline. Each step = "take X → put it in Y". Check off in the app (Today → filters).

## Kitchen zoning (functional, not tidying)
Never just tidy a cabinet in place. First decide each cabinet's job by workflow, then move every item to its job:
- Cook (by the range): D2 utensils + tongs, B2 everyday pots/pans/lids, U3 spices + Shan + ALL oils and vinegars.
- Bake: U4 every baking ingredient, B3 mixing bowls + bakeware, I5 sheet pans/racks/cutting boards.
- Serve (island, where we host): I6 Dutch oven, Le Creuset, cake dome, all serving bowls, chargers; U5 serving boards.
- Dishes by the dishwasher: U7 all plates/bowls; D4 all flatware. Drinks: U8 glasses, mugs, coffee, tea, syrups, bottles.
- Food: P1 snacks + breakfast, P2 rice/grains/bulk, D3 kids' treat drawer (low). Storage: U9 containers + lids, D7 wraps/bags/clips.
- Health high: U10 meds, first aid, vitamins. Clean: B4 cleaning only (locked). Rarely used: U1 appliances, U2 party/seasonal.
- Non-kitchen things leave the pantry (decor, crafts, hats, tools, fragrance).
The item → cabinet map lives in `settings.kitchenPlan.home` (generator: `scripts/kitchen_zoning.py`); moves m40–m74 carry it out. Re-render each cabinet with "take everything out, then place exactly these items", passing reference photos of the items moving in.
