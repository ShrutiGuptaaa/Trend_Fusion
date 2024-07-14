# import pandas as pd
#
# data = [
#     [1, "Wide Leg Jeans", "Bottom Wear", "Jeans", "Spring", 2022, "Denim", "Blue", "Solid", "Casual", "Relaxed Fit", 80, 10000, 500, 10, "https://example.com/jeans.jpg", "Comfortable and stylish jeans for spring", "jeans, wide leg, denim", 5000, 4.5],
#     [2, "Chikankari Kurtas", "Top Wear", "Kurtas", "Summer", 2022, "Cotton", "White", "Floral", "Ethnic", "A-Line", 70, 8000, 300, 8, "https://example.com/kurtas.jpg", "Beautiful hand-embroidered kurtas for summer", "kurtas, chikankari, cotton", 3000, 4.7],
#     [3, "Cord Sets", "Dress", "Sets", "Fall", 2022, "Corduroy", "Brown", "Stripes", "Casual", "Slim Fit", 60, 6000, 200, 6, "https://example.com/cordsets.jpg", "Cozy cord sets for fall", "cord, sets, fall fashion", 2000, 4.2],
#     [4, "Pastel Colors", "Color", "Pastel", "Spring", 2023, "-", "Pastel Pink", "-", "-", "-", 90, 12000, 600, 12, "https://example.com/pastel.jpg", "Soft and soothing pastel colors for spring", "pastel, colors, spring", 7000, 4.8],
#     [5, "Bell Bottoms", "Bottom Wear", "Jeans", "Summer", 2023, "Denim", "Black", "Solid", "Retro", "Flared", 85, 11000, 550, 11, "https://example.com/bellbottoms.jpg", "Groovy bell bottoms for summer", "bell bottoms, jeans, retro", 4500, 4.6],
#     [6, "Silk Blouses", "Top Wear", "Blouses", "Fall", 2022, "Silk", "Red", "Polka Dots", "Formal", "Fitted", 75, 9000, 400, 9, "https://example.com/silkblouses.jpg", "Luxurious silk blouses for fall", "silk, blouses, formal", 3500, 4.4],
#     [7, "Athleisure Wear", "Dress", "Athleisure", "Winter", 2023, "Polyester", "Grey", "Stripes", "Sporty", "Relaxed Fit", 95, 15000, 800, 15, "https://example.com/athleisure.jpg", "Comfortable athleisure wear for winter", "athleisure, sporty, winter", 10000, 4.9],
#     [8, "Ruffled Dresses", "Dress", "Dresses", "Spring", 2022, "Cotton", "Yellow", "Floral", "Feminine", "A-Line", 80, 10000, 500, 10, "https://example.com/ruffledresses.jpg", "Whimsical ruffled dresses for spring", "ruffles, dresses, spring", 5000, 4.6],
#     [9, "Leather Jackets", "Outerwear", "Jackets", "Fall", 2022, "Leather", "Black", "Solid", "Edgy", "Fitted", 85, 11000, 550, 11, "https://example.com/leatherjackets.jpg", "Tough and stylish leather jackets for fall", "leather, jackets, edgy", 4000, 4.7],
#     [10, "Jumpsuits", "Dress", "Jumpsuits", "Summer", 2023, "Cotton", "White", "Solid", "Chic", "Bodycon", 90, 12000, 600, 12, "https://example.com/jumpsuits.jpg", "Stylish and comfortable jumpsuits for summer", "jumpsuits, summer, chic", 7000, 4.8],
#     [11, "High-Waisted Pants", "Bottom Wear", "Pants", "Spring", 2022, "Denim", "Blue", "Solid", "Casual", "High-Waisted", 75, 9000, 400, 9, "https://example.com/highwaisted.jpg", "Trendy high-waisted pants for spring", "high-waisted, pants, denim", 3000, 4.3],
#     [12, "Crochet Tops", "Top Wear", "Tops", "Summer", 2022, "Cotton", "White", "Floral", "Bohemian", "Relaxed Fit", 70, 8000, 300, 8, "https://example.com/crochet.jpg", "Handmade crochet tops for summer", "crochet, tops, bohemian", 2500, 4.5],
#     [13, "Tie-Dye Shirts", "Top Wear", "Shirts", "Summer", 2022, "Cotton", "Multicolor", "Tie-Dye", "Casual", "Relaxed Fit", 85, 11000, 550, 11, "https://example.com/tiedye.jpg", "Colorful tie-dye shirts for summer", "tie-dye, shirts, casual", 4500, 4.7],
#     [14, "Plaid Flannel Shirts", "Top Wear", "Shirts", "Fall", 2022, "Cotton", "Red", "Plaid", "Casual", "Relaxed Fit", 80, 10000, 500, 10, "https://example.com/plaid.jpg", "Cozy plaid flannel shirts for fall", "plaid, shirts, casual", 4000, 4.6],
#     [15, "Cargo Pants", "Bottom Wear", "Pants", "Spring", 2023, "Cotton", "Green", "Solid", "Casual", "Loose Fit", 75, 9000, 400, 9, "https://example.com/cargo.jpg", "Functional cargo pants for spring", "cargo, pants, casual", 3000, 4.4],
#     [16, "Maxi Dresses", "Dress", "Dresses", "Summer", 2023, "Cotton", "Blue", "Floral", "Feminine", "Flowy", 90, 12000, 600, 12, "https://example.com/maxi.jpg", "Elegant maxi dresses for summer", "maxi, dresses, feminine", 6000, 4.8],
#     [17, "Bomber Jackets", "Outerwear", "Jackets", "Fall", 2022, "Polyester", "Green", "Solid", "Casual", "Fitted", 85, 11000, 550, 11, "https://example.com/bomber.jpg", "Trendy bomber jackets for fall", "bomber, jackets, casual", 4500, 4.7],
#     [18, "Puffer Jackets", "Outerwear", "Jackets", "Winter", 2023, "Nylon", "Black", "Solid", "Casual", "Oversized", 90, 13000, 650, 13, "https://example.com/puffer.jpg", "Warm puffer jackets for winter", "puffer, jackets, casual", 7500, 4.9],
#     [19, "Oversized Hoodies", "Top Wear", "Hoodies", "Fall", 2022, "Cotton", "Grey", "Solid", "Casual", "Oversized", 80, 10000, 500, 10, "https://example.com/oversized.jpg", "Comfortable oversized hoodies for fall", "hoodies, casual, oversized", 5000, 4.6],
#     [20, "Skinny Jeans", "Bottom Wear", "Jeans", "Winter", 2023, "Denim", "Black", "Solid", "Casual", "Fitted", 85, 11000, 550, 11, "https://example.com/skinny.jpg", "Trendy skinny jeans for winter", "skinny, jeans, casual", 4000, 4.5],
#     [21, "Midi Skirts", "Bottom Wear", "Skirts", "Spring", 2023, "Cotton", "Pink", "Solid", "Feminine", "A-Line", 90, 12000, 600, 12, "https://example.com/midi.jpg", "Chic midi skirts for spring", "midi, skirts, feminine", 5500, 4.8],
#     [22, "Ankle Boots", "Footwear", "Boots", "Fall", 2022, "Leather", "Black", "Solid", "Casual", "Ankle", 85, 11000, 550, 11, "https://example.com/ankleboots.jpg", "Stylish ankle boots for fall", "ankle boots, casual, fall", 4500, 4.7],
#     [23, "Wide Brim Hats", "Accessories", "Hats", "Summer", 2023, "Straw", "Beige", "Solid", "Casual", "Wide Brim", 75, 9000, 400, 9, "https://example.com/widebrim.jpg", "Trendy wide brim hats for summer", "hats, wide brim, casual", 3500, 4.4],
#     [24, "Denim Shorts", "Bottom Wear", "Shorts", "Summer", 2023, "Denim", "Blue", "Solid", "Casual", "Fitted", 80, 10000, 500, 10, "https://example.com/shorts.jpg", "Comfortable denim shorts for summer", "shorts, denim, casual", 4000, 4.6],
#     [25, "Blazer Dresses", "Dress", "Dresses", "Winter", 2023, "Polyester", "Black", "Solid", "Formal", "Fitted", 90, 13000, 650, 12, "https://example.com/blazerdress.jpg", "Chic blazer dresses for winter", "blazer, dresses, formal", 7000, 4.9],
#     [26, "Kimono Cardigans", "Outerwear", "Cardigans", "Spring", 2023, "Cotton", "White", "Floral", "Bohemian", "Loose Fit", 75, 9000, 400, 9, "https://example.com/kimono.jpg", "Stylish kimono cardigans for spring", "kimono, cardigans, bohemian", 3500, 4.5],
#     [27, "Espadrilles", "Footwear", "Shoes", "Summer", 2023, "Canvas", "Beige", "Solid", "Casual", "Flat", 80, 10000, 500, 10, "https://example.com/espadrilles.jpg", "Comfortable espadrilles for summer", "espadrilles, shoes, casual", 4000, 4.6],
#     [28, "Button-Up Shirts", "Top Wear", "Shirts", "Fall", 2022, "Cotton", "Blue", "Solid", "Casual", "Fitted", 85, 11000, 550, 11, "https://example.com/buttonup.jpg", "Classic button-up shirts for fall", "button-up, shirts, casual", 4500, 4.7],
#     [29, "Faux Leather Leggings", "Bottom Wear", "Leggings", "Winter", 2023, "Faux Leather", "Black", "Solid", "Casual", "Fitted", 90, 13000, 650, 13, "https://example.com/fauxleather.jpg", "Trendy faux leather leggings for winter", "faux leather, leggings, casual", 6000, 4.8],
#     [30, "Graphic Tees", "Top Wear", "T-Shirts", "Spring", 2023, "Cotton", "White", "Graphic", "Casual", "Relaxed Fit", 80, 10000, 500, 10, "https://example.com/graphictees.jpg", "Trendy graphic tees for spring", "graphic, tees, casual", 4000, 4.6],
#     [31, "Sweater Dresses", "Dress", "Dresses", "Winter", 2023, "Wool", "Grey", "Solid", "Casual", "Fitted", 90, 13000, 650, 13, "https://example.com/sweaterdress.jpg", "Warm sweater dresses for winter", "sweater, dresses, casual", 7000, 4.9],
#     [32, "Chino Pants", "Bottom Wear", "Pants", "Spring", 2023, "Cotton", "Beige", "Solid", "Casual", "Slim Fit", 75, 9000, 400, 9, "https://example.com/chino.jpg", "Classic chino pants for spring", "chino, pants, casual", 3500, 4.5],
#     [33, "Lace Dresses", "Dress", "Dresses", "Summer", 2023, "Lace", "White", "Solid", "Feminine", "A-Line", 85, 11000, 550, 11, "https://example.com/lace.jpg", "Elegant lace dresses for summer", "lace, dresses, feminine", 5000, 4.7],
#     [34, "Sherpa Jackets", "Outerwear", "Jackets", "Winter", 2023, "Sherpa", "White", "Solid", "Casual", "Oversized", 90, 13000, 650, 14, "https://example.com/sherpa.jpg", "Cozy sherpa jackets for winter", "sherpa, jackets, casual", 7000, 4.9],
#     [35, "Peasant Tops", "Top Wear", "Tops", "Spring", 2023, "Cotton", "Yellow", "Floral", "Bohemian", "Relaxed Fit", 75, 9000, 400, 9, "https://example.com/peasant.jpg", "Boho peasant tops for spring", "peasant, tops, bohemian", 3500, 4.4],
#     [36, "Wide Leg Trousers", "Bottom Wear", "Trousers", "Fall", 2022, "Polyester", "Grey", "Solid", "Formal", "Wide Leg", 80, 10000, 500, 10, "https://example.com/wideleg.jpg", "Stylish wide leg trousers for fall", "wide leg, trousers, formal", 4000, 4.6],
#     [37, "Kimono Dresses", "Dress", "Dresses", "Summer", 2023, "Silk", "Red", "Floral", "Feminine", "Wrap", 85, 11000, 550, 11, "https://example.com/kimonodress.jpg", "Elegant kimono dresses for summer", "kimono, dresses, feminine", 5000, 4.7],
#     [38, "Pencil Skirts", "Bottom Wear", "Skirts", "Winter", 2023, "Polyester", "Black", "Solid", "Formal", "Fitted", 90, 13000, 650, 12, "https://example.com/pencil.jpg", "Chic pencil skirts for winter", "pencil, skirts, formal", 6000, 4.8],
#     [39, "Flannel Pajamas", "Sleepwear", "Pajamas", "Winter", 2023, "Flannel", "Red", "Plaid", "Casual", "Relaxed Fit", 85, 11000, 550, 11, "https://example.com/pajamas.jpg", "Cozy flannel pajamas for winter", "pajamas, flannel, casual", 4500, 4.7],
#     [40, "Chiffon Blouses", "Top Wear", "Blouses", "Spring", 2023, "Chiffon", "Pink", "Solid", "Feminine", "Loose Fit", 80, 10000, 500, 10, "https://example.com/chiffon.jpg", "Elegant chiffon blouses for spring", "chiffon, blouses, feminine", 4000, 4.6],
#     [41, "Turtleneck Sweaters", "Top Wear", "Sweaters", "Fall", 2022, "Wool", "Brown", "Solid", "Casual", "Fitted", 90, 13000, 650, 14, "https://example.com/turtleneck.jpg", "Warm turtleneck sweaters for fall", "turtleneck, sweaters, casual", 7000, 4.9],
#     [42, "Denim Jackets", "Outerwear", "Jackets", "Spring", 2023, "Denim", "Blue", "Solid", "Casual", "Fitted", 85, 11000, 550, 12, "https://example.com/denimjacket.jpg", "Classic denim jackets for spring", "denim, jackets, casual", 5000, 4.7],
#     [43, "Wrap Dresses", "Dress", "Dresses", "Summer", 2023, "Cotton", "Blue", "Solid", "Feminine", "Wrap", 80, 10000, 500, 10, "https://example.com/wrapdress.jpg", "Chic wrap dresses for summer", "wrap, dresses, feminine", 4500, 4.6],
#     [44, "Platform Sneakers", "Footwear", "Sneakers", "Fall", 2022, "Canvas", "White", "Solid", "Casual", "Platform", 75, 9000, 400, 9, "https://example.com/platform.jpg", "Trendy platform sneakers for fall", "platform, sneakers, casual", 3500, 4.4],
#     [45, "Pleated Skirts", "Bottom Wear", "Skirts", "Spring", 2023, "Polyester", "Pink", "Solid", "Feminine", "Pleated", 80, 10000, 500, 10, "https://example.com/pleated.jpg", "Chic pleated skirts for spring", "pleated, skirts, feminine", 4000, 4.6],
#     [46, "Chunky Sweaters", "Top Wear", "Sweaters", "Winter", 2023, "Wool", "Grey", "Solid", "Casual", "Oversized", 85, 11000, 550, 11, "https://example.com/chunky.jpg", "Cozy chunky sweaters for winter", "chunky, sweaters, casual", 4500, 4.7],
#     [47, "Harem Pants", "Bottom Wear", "Pants", "Summer", 2023, "Cotton", "Black", "Solid", "Casual", "Loose Fit", 70, 8000, 300, 8, "https://example.com/harem.jpg", "Comfortable harem pants for summer", "harem, pants, casual", 3000, 4.5],
#     [48, "Bardot Tops", "Top Wear", "Tops", "Spring", 2023, "Cotton", "White", "Solid", "Feminine", "Off-Shoulder", 75, 9000, 400, 9, "https://example.com/bardot.jpg", "Stylish bardot tops for spring", "bardot, tops, feminine", 3500, 4.6],
#     [49, "Bomber Jackets", "Outerwear", "Jackets", "Fall", 2022, "Polyester", "Green", "Solid", "Casual", "Fitted", 85, 11000, 550, 11, "https://example.com/bomber.jpg", "Trendy bomber jackets for fall", "bomber, jackets, casual", 4500, 4.7],
#     [50, "Puffer Jackets", "Outerwear", "Jackets", "Winter", 2023, "Nylon", "Black", "Solid", "Casual", "Oversized", 90, 13000, 650, 13, "https://example.com/puffer.jpg", "Warm puffer jackets for winter", "puffer, jackets, casual", 7500, 4.9],
#     [51, "Lace Dresses", "Dress", "Dresses", "Summer", 2023, "Lace", "White", "Solid", "Feminine", "A-Line", 85, 11000, 550, 11, "https://example.com/lace.jpg", "Elegant lace dresses for summer", "lace, dresses, feminine", 5000, 4.7],
#     [52, "Sherpa Jackets", "Outerwear", "Jackets", "Winter", 2023, "Sherpa", "White", "Solid", "Casual", "Oversized", 90, 13000, 650, 14, "https://example.com/sherpa.jpg", "Cozy sherpa jackets for winter", "sherpa, jackets, casual", 7000, 4.9],
#     [53, "Kimono Cardigans", "Outerwear", "Cardigans", "Spring", 2023, "Cotton", "White", "Floral", "Bohemian", "Loose Fit", 75, 9000, 400, 9, "https://example.com/kimono.jpg", "Stylish kimono cardigans for spring", "kimono, cardigans, bohemian", 3500, 4.5],
#     [54, "Espadrilles", "Footwear", "Shoes", "Summer", 2023, "Canvas", "Beige", "Solid", "Casual", "Flat", 80, 10000, 500, 10, "https://example.com/espadrilles.jpg", "Comfortable espadrilles for summer", "espadrilles, shoes, casual", 4000, 4.6],
#     [55, "Button-Up Shirts", "Top Wear", "Shirts", "Fall", 2022, "Cotton", "Blue", "Solid", "Casual", "Fitted", 85, 11000, 550, 11, "https://example.com/buttonup.jpg", "Classic button-up shirts for fall", "button-up, shirts, casual", 4500, 4.7],
#     [56, "Pleated Skirts", "Bottom Wear", "Skirts", "Spring", 2023, "Polyester", "Pink", "Solid", "Feminine", "Pleated", 80, 10000, 500, 10, "https://example.com/pleated.jpg", "Chic pleated skirts for spring", "pleated, skirts, feminine", 4000, 4.6],
#     [57, "Chiffon Blouses", "Top Wear", "Blouses", "Spring", 2023, "Chiffon", "Pink", "Solid", "Feminine", "Loose Fit", 80, 10000, 500, 10, "https://example.com/chiffon.jpg", "Elegant chiffon blouses for spring", "chiffon, blouses, feminine", 4000, 4.6],
#     [58, "Turtleneck Sweaters", "Top Wear", "Sweaters", "Fall", 2022, "Wool", "Brown", "Solid", "Casual", "Fitted", 90, 13000, 650, 14, "https://example.com/turtleneck.jpg", "Warm turtleneck sweaters for fall", "turtleneck, sweaters, casual", 7000, 4.9],
#     [59, "Wide Leg Trousers", "Bottom Wear", "Trousers", "Fall", 2022, "Polyester", "Grey", "Solid", "Formal", "Wide Leg", 80, 10000, 500, 10, "https://example.com/wideleg.jpg", "Stylish wide leg trousers for fall", "wide leg, trousers, formal", 4000, 4.6],
#     [60, "Faux Leather Leggings", "Bottom Wear", "Leggings", "Winter", 2023, "Faux Leather", "Black", "Solid", "Casual", "Fitted", 90, 13000, 650, 13, "https://example.com/fauxleather.jpg", "Trendy faux leather leggings for winter", "faux leather, leggings, casual", 6000, 4.8],
#     [61, "Silk Scarves", "Accessories", "Scarves", "Spring", 2023, "Silk", "Red", "Solid", "Formal", "Long", 85, 11000, 550, 12, "https://example.com/silkscarves.jpg", "Elegant silk scarves for spring", "silk, scarves, formal", 5000, 4.8],
#     [62, "Cargo Pants", "Bottom Wear", "Pants", "Fall", 2022, "Cotton", "Green", "Solid", "Casual", "Loose Fit", 80, 10000, 500, 10, "https://example.com/cargo.jpg", "Trendy cargo pants for fall", "cargo, pants, casual", 4500, 4.6],
#     [63, "Tweed Blazers", "Outerwear", "Blazers", "Winter", 2023, "Tweed", "Grey", "Solid", "Formal", "Fitted", 90, 13000, 650, 13, "https://example.com/tweed.jpg", "Chic tweed blazers for winter", "tweed, blazers, formal", 7000, 4.9],
#     [64, "Velvet Dresses", "Dress", "Dresses", "Winter", 2023, "Velvet", "Red", "Solid", "Formal", "Fitted", 85, 11000, 550, 11, "https://example.com/velvet.jpg", "Luxurious velvet dresses for winter", "velvet, dresses, formal", 6000, 4.7],
#     [65, "Ankle Boots", "Footwear", "Boots", "Fall", 2022, "Leather", "Brown", "Solid", "Casual", "Ankle", 80, 10000, 500, 10, "https://example.com/ankleboots.jpg", "Stylish ankle boots for fall", "ankle, boots, casual", 5000, 4.6],
#     [66, "Floral Maxi Dresses", "Dress", "Dresses", "Spring", 2023, "Cotton", "Blue", "Floral", "Feminine", "Maxi", 85, 11000, 550, 12, "https://example.com/floralmaxi.jpg", "Beautiful floral maxi dresses for spring", "floral, maxi, feminine", 6000, 4.8],
#     [67, "Quilted Jackets", "Outerwear", "Jackets", "Winter", 2023, "Polyester", "Black", "Solid", "Casual", "Quilted", 90, 13000, 650, 13, "https://example.com/quilted.jpg", "Warm quilted jackets for winter", "quilted, jackets, casual", 7000, 4.9],
#     [68, "Slouchy Beanies", "Accessories", "Hats", "Winter", 2023, "Wool", "Grey", "Solid", "Casual", "Slouchy", 75, 9000, 400, 9, "https://example.com/beanies.jpg", "Cozy slouchy beanies for winter", "beanies, hats, casual", 4000, 4.5],
#     [69, "Off-Shoulder Dresses", "Dress", "Dresses", "Summer", 2023, "Cotton", "White", "Solid", "Feminine", "Off-Shoulder", 85, 11000, 550, 11, "https://example.com/offshoulder.jpg", "Chic off-shoulder dresses for summer", "off-shoulder, dresses, feminine", 5000, 4.7],
#     [70, "Hiking Boots", "Footwear", "Boots", "Fall", 2022, "Leather", "Brown", "Solid", "Sporty", "Ankle", 80, 10000, 500, 10, "https://example.com/hikingboots.jpg", "Durable hiking boots for fall", "hiking, boots, sporty", 4500, 4.6],
#     [71, "Knitted Cardigans", "Outerwear", "Cardigans", "Winter", 2023, "Wool", "Beige", "Solid", "Casual", "Loose Fit", 90, 13000, 650, 13, "https://example.com/knitted.jpg", "Warm knitted cardigans for winter", "knitted, cardigans, casual", 7000, 4.9],
#     [72, "Bell Sleeve Tops", "Top Wear", "Tops", "Spring", 2023, "Cotton", "Pink", "Solid", "Feminine", "Bell Sleeve", 85, 11000, 550, 12, "https://example.com/bell.jpg", "Trendy bell sleeve tops for spring", "bell sleeve, tops, feminine", 5000, 4.8],
#     [73, "Utility Chic", "Top Wear", "Jackets", "Spring", 2023, "Cotton", "Khaki", "Solid", "Casual", "Oversized", 80, 10000, 500, 10, "https://example.com/utilitychic.jpg", "Functional and stylish utility chic jackets for spring", "utility chic, jackets, spring",4600,3.8],
#     [74, "Asymmetrical Dresses", "Dress", "Dresses", "Summer", 2023, "Silk", "Red", "Floral", "Feminine", "Asymmetrical", 85, 11000, 550, 11, "https://example.com/asymmetricaldresses.jpg", "Elegant and eye-catching asymmetrical dresses for summer", "asymmetrical, dresses, summer",5000,4.2],
#     [75, "Cropped Pants", "Bottom Wear", "Pants", "Fall", 2022, "Denim", "Blue", "Solid", "Casual", "Cropped", 75, 9000, 400, 9, "https://example.com/croppedpants.jpg", "Trendy and comfortable cropped pants for fall", "cropped, pants, denim",5500,4.8],
#     [76, "Ruffled Blouses", "Top Wear", "Blouses", "Spring", 2022, "Cotton", "White", "Floral", "Feminine", "Ruffled", 80, 10000, 500, 10, "https://example.com/ruffledblouses.jpg", "Whimsical and romantic ruffled blouses for spring", "ruffles, blouses, spring",5600,4.1],
#     [77, "Biker Shorts", "Bottom Wear", "Shorts", "Summer", 2023, "Polyester", "Black", "Solid", "Sporty", "Fitted", 90, 12000, 600, 12, "https://example.com/bikershorts.jpg", "Comfortable and stylish biker shorts for summer", "biker, shorts, summer",6000,4.4],
#     [78, "Puff Sleeves", "Top Wear", "Tops", "Fall", 2022, "Cotton", "Yellow", "Solid", "Casual", "Puff Sleeves", 70, 8000, 300, 8, "https://example.com/puffsleeves.jpg", "Trendy and cozy puff sleeves for fall", "puff sleeves, tops, fall",7000,4.4],
#     [79, "High-Low Dresses", "Dress", "Dresses", "Spring", 2022, "Silk", "Pink", "Floral", "Feminine", "High-Low", 85, 11000, 550, 11, "https://example.com/highlowdresses.jpg", "Elegant and stylish high-low dresses for spring", "high-low, dresses, spring",6000,3.9],
#     [80, "Corduroy Jackets", "Outerwear", "Jackets", "Fall", 2022, "Corduroy", "Brown", "Solid", "Casual", "Fitted", 75, 9000, 400, 9, "https://example.com/corduroyjackets.jpg", "Cozy and stylish corduroy jackets for fall", "corduroy, jackets, fall",6000,4.3],
#     [81, "Bell Sleeve Tops", "Top Wear", "Tops", "Summer", 2023, "Cotton", "White", "Solid", "Feminine", "Bell Sleeve", 80, 10000, 500, 10, "https://example.com/bellsleeve.jpg", "Whimsical and romantic bell sleeve tops for summer", "bell sleeve, tops, summer",5555,4.3]]
# # Convert to DataFrame
# columns = [
#     'Trend ID', 'Trend Name', 'Trend Type', 'Trend Subtype', 'Season', 'Year', 'Fabric',
#     'Color', 'Pattern', 'Style', 'Silhouette', 'Popularity Score', 'Search Volume',
#     'Social Media Mentions', 'Influencer Endorsements', 'Image URL', 'Description',
#     'Keywords', 'Sales', 'User Rating'
# ]
#
# df = pd.DataFrame(data, columns=columns)
#
# dd a section title
#
# # # Create 2 columns
# # col1, col2 = st.columns(2)
# #
# # # Add images and buttons to each column
# # with col1:
# #     st.image("Images/winter_image.jpeg", width=300, use_column_width=True)
# #     st.write("")  # Add a blank line
# #     if st.button("Get Winter Recommendations"):
# #         # Add code to display winter recommendations here
# #         st.write("Winter recommendations will appear here!")
# #     # st.markdown("---")  # Add horizontal space
# #
# # with col2:
# #     st.image("Images/spring_image.jpeg", width=300, use_column_width=True)
# #     st.write("")  # Add a blank line
# #     if st.button("Get Spring Recommendations"):
# #         # Add code to display spring recommendations here
# #         st.write("Spring recommendations will appear here!")
# #     # st.markdown("---")  # Add horizontal space
# #
# # # Add a horizontal space
# # st.write("")  # Add a blank line
# #
# # # Create 2 columns again
# # col1, col2 = st.columns(2)
# #
# # # Add images and buttons to each column
# # with col1:
# #     st.image("Images/summer_image.jpeg", width=300, use_column_width=True)
# #     st.write("")  # Add a blank line
# #     if st.button("Get Summer Recommendations"):
# #         # Add code to display summer recommendations here
# #         st.write("Summer recommendations will appear here!")
# #     # st.markdown("---")  # Add horizontal space
# #
# # with col2:
# #     st.image("Images/fall_image.jpeg", width=300, use_column_width=True)
# #     st.write("")  # Add a blank line
# #     if st.button("Get Autumn Recommendations"):
# #         # Add code to display autumn recommendations here
# #         st.write("Autumn recommendations will appear here!")
# #     # st.markdown("---")  # Add horizontal space
# # # # Get the selected season
# # # selected_season = st.selectbox("Select a season", df["Season"].unique())
# # #
# # # # Create a button to show the trends
# # # show_trends = st.button("Show Trends")
#
# # Create a function to get top 10 trends based on season and gender
# def get_top_trends(season, gender):
#     season_df = df[df['Season'] == season]
#     gender_df = season_df[season_df['Gender'] == gender]
#     if gender_df.empty:
#         return "No data available for this selection"
#     else:
#         top_trends = gender_df.sort_values(by=['Popularity Score', 'Search Volume', 'Social Media Mentions'], ascending=False).head(10)
#         return top_trends
#
# # Create the main app
# st.title("Fashion Trends")
#
# # Create columns for season buttons
# col1, col2 = st.columns(2)
#
# with col1:
#     st.image("Images/winter_image.jpeg", width=300, use_column_width=True)
#     st.write("")  # Add a blank line
#     if st.button("Get Winter Recommendations"):
#         with st.expander("Winter Recommendations"):
#             gender = st.selectbox("Select Gender", ["Male", "Female"])
#             show_button = st.button("Show")
#             if show_button:
#                 top_trends = get_top_trends("Winter", gender)
#                 if isinstance(top_trends, str):
#                     st.write(top_trends)
#                 else:
#                     trend_names = top_trends['Trend Name'].tolist()
#                     for trend in trend_names:
#                         st.write(trend)
#
# with col2:
#     st.image("Images/spring_image.jpeg", width=300, use_column_width=True)
#     st.write("")  # Add a blank line
#     if st.button("Get Spring Recommendations"):
#         with st.expander("Spring Recommendations"):
#             gender = st.selectbox("Select Gender", ["Male", "Female"])
#             show_button = st.button("Show")
#             if show_button:
#                 top_trends = get_top_trends("Spring", gender)
#                 if isinstance(top_trends, str):
#                     st.write(top_trends)
#                 else:
#                     trend_names = top_trends['Trend Name'].tolist()
#                     for trend in trend_names:
#                         st.write(trend)
#
# # Add a horizontal space
# st.write("")  # Add a blank line
#
# # Create 2 columns again
# col1, col2 = st.columns(2)
#
# # Add images and buttons to each column
# with col1:
#     st.image("Images/summer_image.jpeg", width=300, use_column_width=True)
#     st.write("")  # Add a blank line
#     if st.button("Get Summer Recommendations"):
#         with st.expander("Summer Recommendations"):
#             gender = st.selectbox("Select Gender", ["Male", "Female"])
#             show_button = st.button("Show")
#             if show_button:
#                 top_trends = get_top_trends("Summer", gender)
#                 if isinstance(top_trends, str):
#                     st.write(top_trends)
#                 else:
#                     trend_names = top_trends['Trend Name'].tolist()
#                     for trend in trend_names:
#                         st.write(trend)
#
# with col2:
#     st.image("Images/fall_image.jpeg", width=300, use_column_width=True)
#     st.write("")  # Add a blank line
#     if st.button("Get Autumn Recommendations"):
#         with st.expander("Autumn Recommendations"):
#             gender = st.selectbox("Select Gender", ["Male", "Female"])
#             show_button = st.button("Show")
#             if show_button:
#                 top_trends = get_top_trends("Fall", gender)
#                 if isinstance(top_trends, str):
#                     st.write(top_trends)
#                 else:
#                     trend_names = top_trends['Trend Name'].tolist()
#                     for trend in trend_names:
#                         st.write(trend)
#
# # if show_trends:
# #     # Filter the data for the selected season
# #     season_df = df[df["Season"] == selected_season]
# #
# #     # Sort the data by popularity score, then by search volume
# #     sorted_df = season_df.sort_values(by=["Popularity Score", "Search Volume","Sales"], ascending=False)
# #
# #     # Display the top 5 trends
# #     st.write("Top Trends for", selected_season)
# #     for row in sorted_df.head(10).iterrows():
# #         st.write(f"{row[1]['Trend Name']} ({row[1]['Trend Type']})")
# #         st.image(row[1]["Image URL"])
# #         st.write("Popularity Score:", row[1]["Popularity Score"])
# #         st.write("Social Media Mentions:", row[1]["Social Media Mentions"])
# #         st.write("User Rating:", row[1]["User Rating"])
# #         st.write("-------------------------")
# #
# # # Create a section for trend selection
# # st.subheader("Choose Trend Details")
# #
# # # Get the unique trend types
# # trend_types = df["Trend Type"].unique()
# #
# # # Create a selectbox for trend type
# # trend_type = st.selectbox("Select Trend Type", trend_types)
# #
# # # Filter the data based on the selected trend type
# # filtered_df = df[df["Trend Type"] == trend_type]
# #
# # # Get the unique styles for the selected trend type
# # styles = filtered_df["Style"].unique()
# #
# # # Create a selectbox for style
# # style = st.selectbox("Select Style", styles)
# #
# # # Create a button to get the trend names
# # get_trend_names = st.button("Get Trend Names")
# #
# # if get_trend_names:
# #     # Filter the data based on the selected trend type and style
# #     filtered_df = df[(df["Trend Type"] == trend_type) & (df["Style"] == style)]
# #
# #     # Get the trend names and corresponding images from the filtered data
# #     trend_names = filtered_df["Trend Name"].unique()
# #     trend_image_urls = filtered_df["Image URL"].unique()
# #
# #     # Display the trend names and images
# #     st.write("Trend Names:")
# #     for trend_name, trend_image_url in zip(trend_names, trend_image_urls):
# #         st.write("- ", trend_name)
# #         st.image(trend_image_url, width=200)  # adjust the width as needed
#
