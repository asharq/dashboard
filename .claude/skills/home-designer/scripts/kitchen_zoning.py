import json
D=json.load(open('D.json'));I=D['items']
H={}
def put(cab,*ids):
  for i in ids: assert i in I,i; H[i]=cab
# U1 rarely-used appliances
put("c-u1","uf-instantpot","u4-ricecooker","i-imusa","u4-bonsen","uf-tote")
# U2 party backstock + seasonal
put("c-u2","uf-dinnerware","p-solocups","b1-eid","d3-napkins")
# U3 spices, oils, vinegars, flavor bases
put("c-u3","u3-cardamom","u3-methi","u3-morton","u3-spicerack","u3-bayleaves","u3-pepper","u3-spices","u3-avocadospray","u3-turmeric","u3-tins","u3-cloves","u3-shan","u3-flakes","u3-oilbottle","u3-vinegar","u3-chickenmasala","u3-redpepper","b2-shan","b3-oliveoil","b3-vegoil","u4-ricevinegar","u10-cardamompods","u4-bouillon")
# U4 baking center
put("c-u4","u4-extracts","u4-cocoa","u4-clabber","u4-honey","u4-oxo","u4-bins","u4-waffle","u3-foodcolor","b2-bakingsoda","u10-flour","b2-ziplocs","d3-sprinkles","d3-melting","d7-liners","d3-cutter")
# U5 serving boards
put("c-u5","b1-board")
# U7 everyday dishes
put("c-u7","u7-plates","u7-cereal","u7-melamine","b1-plates","b1-bowls","b1-pasta")
# U8 drinks
put("c-u8","u8-algonquin","u8-stripemugs","u8-rocks","u8-thermos","u8-teajar","u8-tallmug","u8-owala","u8-stirrers","u8-coffeemate","u8-applemugs","u8-campmug","u8-plasticcups","u8-ripple","u4-tea","u4-liquidiv","p-oxo","p-coffeebags","p-torani","p-watkins","p-whitechoc","p-filters","p-bottles","dw-glassmug","d2-barspoon","d2-muddler")
# U9 food storage
put("c-u9","u9-smalldish","u9-bakingdish","u9-lids","u9-snapware","u9-glass","b2-pyrex","dw-pyrex","u4-takeout","b2-mason")
# U10 health, high
put("c-u10","u10-syringes","u10-gloves","u10-alcoholpads","p-coq10","p-coldpack","p-nyquil","p-firstaid","p-multivit","p-benadryl","p-sunscreen","u4-supplement","p-turntable")
# P1 snacks + breakfast
put("c-p1","u10-mac","u10-nuts","u4-pb","u4-oatmeal","u4-popcorn","u4-popseason","b2-oats","d3-walnuts","u4-chilionion")
# P2 grains + bulk + drinks backstock
put("c-p2","b2-rice","u10-bags","u10-seeds","b2-mesh","i-ghi","b2-bags")
# D1 measuring + gadgets
put("c-d1","d1-thermo","d1-manual","d1-liners","d1-cork","d1-scale","d4-measure","u4-skewers")
# D2 cooking utensils
put("c-d2","d2-scoop","d2-canopener","d2-lemon","d2-masher","d2-whisk","d2-brush","d2-pizzacutter","d2-spatulas","d2-ladles","d4-gadgets","d4-rialto")
# D3 girls' treat drawer
put("c-d3","d3-chips","d3-chocbars","d3-hamilton","d3-butterbeer","d3-pinksnack","u4-snackbag")
# D4 flatware
put("c-d4","d4-tray","d4-flatware","d4-chopsticks","u8-crock")
# D5 linens
put("c-d5","d5-potholder","d5-stripetowels","d5-creammitt")
# D6 drying mats
put("c-d6","d6-mats")
# D7 wraps + bags + clips
put("c-d7","d7-wrap","d7-ziploc","d7-parchment","d7-foil","d7-sandwich","d2-clips","d4-blueclip")
# B1 small appliances
put("c-b1","b1-kettle","b1-toaster","b1-blender")
# B2 everyday pots + pans
put("c-b2","i6-skillets","i6-stockpot","i6-colander","i6-panrack","dw-pan","i6-braiser","u4-glasslid","i6-lid")
# B3 mixing + bakeware
put("c-b3","b3-cakepan","b3-bakers","b3-heartdish","b3-funnel","b3-strainer","i6-mixing","dw-mixingbowl","i6-loafpan","i6-muffin")
# B4 cleaning only
put("c-b4","b4-lemon","b4-cascade","b4-floralspray","b4-dustpan","b4-bkf","b4-caddy","b4-squeeze","b4-aerosol","b4-brush","b4-sponges","b4-gloves","b4-redspray","b4-dishrefill","i-trashbags")
# I5 flat bake + prep
put("c-i5","i5-rack","i5-sheetpans","i5-pizza","i5-board","i5-mats","i6-board")
# I6 serving + entertaining
put("c-i6","i6-dutchoven","b3-lecreuset","b3-cakedome","u3-servingbowls","u7-servbowls","u7-floral","u7-small","d5-charger")
# I2 desk / I4 bags / I3 keepsakes
put("c-i2","p-pens","p-markers","p-tape")
put("c-i4","d6-bags")
put("c-i1","d2-opener")
put("c-i3","d3-tin")
# L1 laundry closet: cleaning backstock, tools, fragrance
put("c-l1","p-lysol","p-antspray","p-refillwipes","p-homebin","p-command","p-kingroll","p-diffuser","p-roomspray","p-eucalyptus","p-sandfog","p-amber","b4-lysolbath")
# Off to other rooms (no cabinet): label as destination text
OUT={"p-paintkits":"Kids' art basket (coffee table)","p-canvas":"Kids' art basket (coffee table)","p-basket":"Coffee table lower shelf","p-woodpaint":"Kids' art basket","p-instax":"Island drawer I3","p-capriblue":"Coffee table tray","p-goldholder":"Side table","p-terrarium":"Right side table","p-crystal":"Bedroom dresser","p-velvet":"Bedroom dresser","p-woodstand":"Bedroom dresser","p-motovera":"Island drawer I2","p-bucket":"Bedroom closet","p-jordan":"Bedroom closet","p-mmga":"Bedroom closet","p-hats":"Bedroom closet","b4-vase":"Console table (fresh flowers)","d5-burntmitt":"Toss (scorched)","d7-foilscrap":"Toss","dw-dishwasher":None}
moved={i:c for i,c in H.items() if I[i].get('cab')!=c}
print("assigned",len(H),"moving",len(moved),"out",len(OUT))
# unassigned kitchen items
K=[c for c in D['cabinets'] if D['cabinets'][c]['room'] in('kitchen','island') or c=='c-l1']
un=[i for i,v in I.items() if v.get('cab') in K and i not in H and i not in OUT and v.get('cab') not in('c-fr','c-fz','c-i1','c-i3','c-i4','c-i2','c-l1')]
print("unassigned",un)
json.dump({"home":H,"out":{k:v for k,v in OUT.items() if v}},open('zoning.json','w'))
