import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
import numpy as np


data = [
    [1, "Wide Leg Jeans", "Bottom Wear", "Jeans", "Spring", 2022, "Denim", "Blue", "Solid", "Casual", "Relaxed Fit", 80, 10000, 500, 10, "Images/wide leg jeans.jpeg", "Comfortable and stylish jeans for spring", "jeans, wide leg, denim", 5000, 4.5,"Female"],
    [2, "Chikankari Kurtas", "Top Wear", "Kurtas", "Summer", 2022, "Cotton", "White", "Floral", "Ethnic", "A-Line", 92, 8000, 300, 8, "Images/chikankari.jpeg", "Beautiful hand-embroidered kurtas for summer", "kurtas, chikankari, cotton", 3000, 4.7,"Female"],
    [3, "Cord Sets", "Dress", "Sets", "Fall", 2022, "Corduroy", "Brown", "Stripes", "Casual", "Slim Fit", 60, 6000, 200, 6, "Images/coord_Set.jpeg", "Cozy cord sets for fall", "cord, sets, fall fashion", 2000, 4.2,"Female"],
    # [4, "Pastel Colors", "Color", "Pastel", "Spring", 2023, "-", "Pastel Pink", "-", "-", "-", 90, 12000, 600, 12, "Images/pastel_colors.jpg", "Soft and soothing pastel colors for spring", "pastel, colors, spring", 7000, 4.8,"Female"],
    [5, "Bell Bottoms", "Bottom Wear", "Jeans", "Summer", 2023, "Denim", "Black", "Solid", "Retro", "Flared", 85, 11000, 550, 11, "Images/bell bottoms.jpeg", "Groovy bell bottoms for summer", "bell bottoms, jeans, retro", 4500, 4.6,"Female"],
    [6, "Silk Blouses", "Top Wear", "Blouses", "Fall", 2022, "Silk", "Red", "Polka Dots", "Formal", "Fitted", 75, 9000, 400, 9, "Images/silk blouse.jpeg", "Luxurious silk blouses for fall", "silk, blouses, formal", 3500, 4.4,"Female"],
    [7, "Athleisure Wear", "Casual", "Athleisure", "Winter", 2023, "Polyester", "Grey", "Stripes", "Sporty", "Relaxed Fit", 95, 15000, 800, 15, "Images/athliesure.jpeg", "Comfortable athleisure wear for winter", "athleisure, sporty, winter", 10000, 4.9,"Female"],
    [8, "Ruffled Dresses", "Dress", "Dresses", "Spring", 2022, "Cotton", "Yellow", "Floral", "Feminine", "A-Line", 80, 10000, 500, 10, "Images/ruffke dresses.jpeg", "Whimsical ruffled dresses for spring", "ruffles, dresses, spring", 5000, 4.6,"Female"],
    [9, "Leather Jackets", "Outerwear", "Jackets", "Fall", 2022, "Leather", "Black", "Solid", "Edgy", "Fitted", 85, 11000, 550, 11, "Images/leather.jpeg", "Tough and stylish leather jackets for fall", "leather, jackets, edgy", 4000, 4.7,"Female"],
    [10, "Jumpsuits", "Dress", "Jumpsuits", "Summer", 2023, "Cotton", "White", "Solid", "Chic", "Bodycon", 90, 12000, 600, 12, "Images/jump suit.jpeg", "Stylish and comfortable jumpsuits for summer", "jumpsuits, summer, chic", 7000, 4.8,"Female"],
    [11, "High-Waisted Pants", "Bottom Wear", "Pants", "Spring", 2022, "Denim", "Blue", "Solid", "Casual", "High-Waisted", 75, 9000, 400, 9, "Images/high waisted.jpeg", "Trendy high-waisted pants for spring", "high-waisted, pants, denim", 3000, 4.3,"Female"],
    [12, "Crochet Tops", "Top Wear", "Tops", "Summer", 2022, "Cotton", "White", "Floral", "Bohemian", "Relaxed Fit", 94, 8000, 300, 8, "Images/crochet tops.jpeg", "Handmade crochet tops for summer", "crochet, tops, bohemian", 2500, 4.5,"Female"],
    [13, "Tie-Dye Shirts", "Top Wear", "Shirts", "Summer", 2022, "Cotton", "Multicolor", "Tie-Dye", "Casual", "Relaxed Fit", 85, 11000, 550, 11, "Images/tie dye.jpeg", "Colorful tie-dye shirts for summer", "tie-dye, shirts, casual", 4500, 4.7,"Female"],
    [14, "Plaid Flannel Shirts", "Casual", "Shirts", "Fall", 2022, "Cotton", "Red", "Plaid", "Casual", "Relaxed Fit", 80, 10000, 500, 10, "Images/plaid fannel.jpeg", "Cozy plaid flannel shirts for fall", "plaid, shirts, casual", 4000, 4.6,"Female"],
    [15, "Cargo Pants", "Bottom Wear", "Pants", "Spring", 2023, "Cotton", "Green", "Solid", "Casual", "Loose Fit", 75, 9000, 400, 9, "Images/cargo pants.jpeg", "Functional cargo pants for spring", "cargo, pants, casual", 3000, 4.4,"Female"],
    [16, "Maxi Dresses", "Dress", "Dresses", "Summer", 2023, "Cotton", "Blue", "Floral", "Feminine", "Flowy", 95, 12000, 600, 12, "Images/maxi dress.jpeg", "Elegant maxi dresses for summer", "maxi, dresses, feminine", 6000, 4.8,"Female"],
    [17, "Bomber Jackets", "Outerwear", "Jackets", "Fall", 2022, "Polyester", "Green", "Solid", "Casual", "Fitted", 85, 11000, 550, 11, "Images/bomber jacket.jpeg", "Trendy bomber jackets for fall", "bomber, jackets, casual", 4500, 4.7,"Female"],
    [18, "Puffer Jackets", "Outerwear", "Jackets", "Winter", 2023, "Nylon", "Black", "Solid", "Casual", "Oversized", 90, 13000, 650, 13, "Images/puffer jacket.jpeg", "Warm puffer jackets for winter", "puffer, jackets, casual", 7500, 4.9,"Female"],
    [19, "Oversized Hoodies", "Top Wear", "Hoodies", "Fall", 2022, "Cotton", "Grey", "Solid", "Casual", "Oversized", 80, 10000, 500, 10, "Images/oversized hoodies .jpeg", "Comfortable oversized hoodies for fall", "hoodies, casual, oversized", 5000, 4.6,"Female"],
    [20, "Skinny Jeans", "Bottom Wear", "Jeans", "Winter", 2023, "Denim", "Black", "Solid", "Casual", "Fitted", 85, 11000, 550, 11, "Images/skinny jeans.jpeg", "Trendy skinny jeans for winter", "skinny, jeans, casual", 4000, 4.5,"Female"],
    [21, "Midi Skirts", "Bottom Wear", "Skirts", "Spring", 2023, "Cotton", "Pink", "Solid", "Feminine", "A-Line", 90, 12000, 600, 12, "Images/midi skirts.jpeg", "Chic midi skirts for spring", "midi, skirts, feminine", 5500, 4.8,"Female"],
    [22, "Ankle Boots", "Footwear", "Boots", "Fall", 2022, "Leather", "Black", "Solid", "Casual", "Ankle", 85, 11000, 550, 11, "Images/ankle boots.jpeg", "Stylish ankle boots for fall", "ankle boots, casual, fall", 4500, 4.7,"Female"],
    [23, "Wide Brim Hats", "Accessories", "Hats", "Summer", 2023, "Straw", "Beige", "Solid", "Casual", "Wide Brim", 75, 9000, 400, 9, "Images/wide brim.jpeg", "Trendy wide brim hats for summer", "hats, wide brim, casual", 3500, 4.4,"Female"],
    [24, "Denim Shorts", "Bottom Wear", "Shorts", "Summer", 2023, "Denim", "Blue", "Solid", "Casual", "Fitted", 80, 10000, 500, 10, "Images/denim shorts.jpeg", "Comfortable denim shorts for summer", "shorts, denim, casual", 4000, 4.6,"Female"],
    [25, "Blazer Dresses", "Dress", "Dresses", "Winter", 2023, "Polyester", "Black", "Solid", "Formal", "Fitted", 90, 13000, 650, 12, "Images/blazer dress.jpeg", "Chic blazer dresses for winter", "blazer, dresses, formal", 7000, 4.9,"Female"],
    [26, "Kimono Cardigans", "Outerwear", "Cardigans", "Spring", 2023, "Cotton", "White", "Floral", "Bohemian", "Loose Fit", 75, 9000, 400, 9, "Images/kimono.jpeg", "Stylish kimono cardigans for spring", "kimono, cardigans, bohemian", 3500, 4.5,"Female"],
    [27, "Espadrilles", "Footwear", "Shoes", "Summer", 2023, "Canvas", "Beige", "Solid", "Casual", "Flat", 80, 10000, 500, 10, "Images/espadriel.jpeg", "Comfortable espadrilles for summer", "espadrilles, shoes, casual", 4000, 4.6,"Female"],
    [28, "Button-Up Shirts", "Casual", "Shirts", "Fall", 2022, "Cotton", "Blue", "Solid", "Casual", "Fitted", 85, 11000, 550, 11, "Images/buttonup shirts.jpeg", "Classic button-up shirts for fall", "button-up, shirts, casual", 4500, 4.7,"Female"],
    [29, "Faux Leather Leggings", "Bottom Wear", "Leggings", "Winter", 2023, "Faux Leather", "Black", "Solid", "Casual", "Fitted", 90, 13000, 650, 13, "Images/faux leggings.jpeg", "Trendy faux leather leggings for winter", "faux leather, leggings, casual", 6000, 4.8,"Female"],
    [30, "Graphic Tees", "Top Wear", "T-Shirts", "Spring", 2023, "Cotton", "White", "Graphic", "Casual", "Relaxed Fit", 80, 10000, 500, 10, "Images/graphic tees.jpeg", "Trendy graphic tees for spring", "graphic, tees, casual", 4000, 4.6,"Female"],
    [31, "Sweater Dresses", "Dress", "Dresses", "Winter", 2023, "Wool", "Grey", "Solid", "Casual", "Fitted", 90, 13000, 650, 13, "Images/sweater dress.jpeg", "Warm sweater dresses for winter", "sweater, dresses, casual", 7000, 4.9,"Female"],
    [32, "Chino Pants", "Bottom Wear", "Pants", "Spring", 2023, "Cotton", "Beige", "Solid", "Casual", "Slim Fit", 75, 9000, 400, 9, "Images/chino pants.jpeg", "Classic chino pants for spring", "chino, pants, casual", 3500, 4.5,"Female"],
    [33, "Lace Dresses", "Dress", "Dresses", "Summer", 2023, "Lace", "White", "Solid", "Feminine", "A-Line", 92, 11000, 550, 11, "Images/lace dresses.jpeg", "Elegant lace dresses for summer", "lace, dresses, feminine", 5000, 4.7,"Female"],
    [34, "Sherpa Jackets", "Outerwear", "Jackets", "Winter", 2023, "Sherpa", "White", "Solid", "Casual", "Oversized", 90, 13000, 650, 14, "Images/sherpa jacket.jpeg", "Cozy sherpa jackets for winter", "sherpa, jackets, casual", 7000, 4.9,"Female"],
    [35, "Peasant Tops", "Top Wear", "Tops", "Spring", 2023, "Cotton", "Yellow", "Floral", "Bohemian", "Relaxed Fit", 75, 9000, 400, 9, "Images/peasant tops.jpeg", "Boho peasant tops for spring", "peasant, tops, bohemian", 3500, 4.4,"Female"],
    [36, "Wide Leg Trousers", "Casual", "Trousers", "Fall", 2022, "Polyester", "Grey", "Solid", "Formal", "Wide Leg", 80, 10000, 500, 10, "Images/wide leg trousers.jpeg", "Stylish wide leg trousers for fall", "wide leg, trousers, formal", 4000, 4.6,"Female"],
    [37, "Kimono Dresses", "Dress", "Dresses", "Summer", 2023, "Silk", "Red", "Floral", "Feminine", "Wrap", 85, 11000, 550, 11, "Images/kimono dress.jpeg", "Elegant kimono dresses for summer", "kimono, dresses, feminine", 5000, 4.7,"Female"],
    [38, "Pencil Skirts", "Bottom Wear", "Skirts", "Winter", 2023, "Polyester", "Black", "Solid", "Formal", "Fitted", 90, 13000, 650, 12, "Images/pencil skirts.jpeg", "Chic pencil skirts for winter", "pencil, skirts, formal", 6000, 4.8,"Female"],
    [39, "Flannel Pajamas", "Sleepwear", "Pajamas", "Winter", 2023, "Flannel", "Red", "Plaid", "Casual", "Relaxed Fit", 85, 11000, 550, 11, "Images/flannel pajamasjpeg.jpeg", "Cozy flannel pajamas for winter", "pajamas, flannel, casual", 4500, 4.7,"Female"],
    [40, "Chiffon Blouses", "Top Wear", "Blouses", "Spring", 2023, "Chiffon", "Pink", "Solid", "Feminine", "Loose Fit", 80, 10000, 500, 10, "Images/chiffon blouses.jpeg", "Elegant chiffon blouses for spring", "chiffon, blouses, feminine", 4000, 4.6,"Female"],
    [41, "Turtleneck Sweaters", "Top Wear", "Sweaters", "Fall", 2022, "Wool", "Brown", "Solid", "Casual", "Fitted", 90, 13000, 650, 14, "Images/turtle necks.jpeg", "Warm turtleneck sweaters for fall", "turtleneck, sweaters, casual", 7000, 4.9,"Female"],
    [42, "Denim Jackets", "Outerwear", "Jackets", "Spring", 2023, "Denim", "Blue", "Solid", "Casual", "Fitted", 85, 11000, 550, 12, "Images/denim jackets.jpeg", "Classic denim jackets for spring", "denim, jackets, casual", 5000, 4.7,"Female"],
    [43, "Wrap Dresses", "Dress", "Dresses", "Summer", 2023, "Cotton", "Blue", "Solid", "Feminine", "Wrap", 80, 10000, 500, 10, "Images/wrap dresses.jpeg", "Chic wrap dresses for summer", "wrap, dresses, feminine", 4500, 4.6,"Female"],
    [44, "Platform Sneakers", "Footwear", "Sneakers", "Fall", 2022, "Canvas", "White", "Solid", "Casual", "Platform", 75, 9000, 400, 9, "Images/platform sneakers.jpeg", "Trendy platform sneakers for fall", "platform, sneakers, casual", 3500, 4.4,"Female"],
    [45, "Pleated Skirts", "Bottom Wear", "Skirts", "Spring", 2023, "Polyester", "Pink", "Solid", "Feminine", "Pleated", 80, 10000, 500, 10, "Images/pleated skirts.jpeg", "Chic pleated skirts for spring", "pleated, skirts, feminine", 4000, 4.6,"Female"],
    [46, "Chunky Sweaters", "Top Wear", "Sweaters", "Winter", 2023, "Wool", "Grey", "Solid", "Casual", "Oversized", 85, 11000, 550, 11, "Images/chunky sweaters.jpeg", "Cozy chunky sweaters for winter", "chunky, sweaters, casual", 4500, 4.7,"Female"],
    [47, "Harem Pants", "Bottom Wear", "Pants", "Summer", 2023, "Cotton", "Black", "Solid", "Casual", "Loose Fit", 70, 8000, 300, 8, "Images/harem pants.jpeg", "Comfortable harem pants for summer", "harem, pants, casual", 3000, 4.5,"Female"],
    [48, "Bardot Tops", "Top Wear", "Tops", "Spring", 2023, "Cotton", "White", "Solid", "Feminine", "Off-Shoulder", 88, 9000, 400, 9, "Images/bardot tops.jpeg", "Stylish bardot tops for spring", "bardot, tops, feminine", 3500, 4.6,"Female"],
    [49, "Bomber Jackets", "Outerwear", "Jackets", "Fall", 2022, "Polyester", "Green", "Solid", "Casual", "Fitted", 85, 11000, 550, 11, "Images/bomber jacket1.jpeg", "Trendy bomber jackets for fall", "bomber, jackets, casual", 4500, 4.7,"Female"],
    [50, "Puffer Jackets", "Outerwear", "Jackets", "Winter", 2023, "Nylon", "Black", "Solid", "Casual", "Oversized", 90, 13000, 650, 13, "Images/puffer jacket.jpeg", "Warm puffer jackets for winter", "puffer, jackets, casual", 7500, 4.9,"Female"],

    [51, "Slim Fit Chinos", "Bottom Wear", "Chinos", "Summer", 2022, "Cotton", "Beige", "Solid", "Casual", "Slim Fit", 85, 12000, 600, 15, "Images/slim fit chinos.jpeg", "Trendy and comfortable chinos for summer", "chinos, slim fit, cotton", 5500, 4.6,"Male"],
    [52, "Graphic Tee", "Top Wear", "T-shirt", "Spring", 2022, "Cotton", "White", "Graphic", "Casual", "Regular Fit", 87, 15000, 800, 20, "Images/graphic tee.jpeg", "Cool graphic tee for casual wear", "t-shirt, graphic, casual", 7000, 4.7,"Male"],
    [53, "Bomber Jacket", "Outerwear", "Jacket", "Fall", 2022, "Polyester", "Black", "Solid", "Casual", "Regular Fit", 75, 11000, 700, 12, "Images/bomber jacket men.jpeg", "Stylish bomber jacket for fall", "jacket, bomber, casual", 5200, 4.4,"Male"],
    [54, "Linen Shirt", "Top Wear", "Shirt", "Summer", 2022, "Linen", "Light Blue", "Solid", "Casual", "Regular Fit", 88, 13000, 750, 18, "Images/linen shirt.jpeg", "Lightweight linen shirt for summer", "shirt, linen, casual", 6300, 4.6,"Male"],
    [55, "Cargo Pants", "Bottom Wear", "Pants", "Spring", 2022, "Cotton", "Olive Green", "Solid", "Casual", "Loose Fit", 82, 10500, 650, 14, "Images/cargo pants men.jpeg", "Practical and trendy cargo pants", "pants, cargo, casual", 5400, 4.5,"Male"],
    [56, "Denim Jacket", "Outerwear", "Jacket", "Spring", 2022, "Denim", "Blue", "Solid", "Casual", "Regular Fit", 87, 14000, 850, 25, "Images/denim jacket.jpeg", "Classic denim jacket for spring", "jacket, denim, casual", 6800, 4.7,"Male"],
    [57, "Henley Shirt", "Top Wear", "Shirt", "Fall", 2022, "Cotton", "Gray", "Solid", "Casual", "Regular Fit", 78, 9000, 550, 10, "Images/henley shirt.jpeg", "Comfortable henley shirt for fall", "shirt, henley, casual", 4700, 4.3,"Male"],
    [58, "Jogger Pants", "Sportswear", "Pants", "Winter", 2022, "Polyester", "Black", "Solid", "Casual", "Slim Fit", 83, 11000, 700, 16, "Images/jogger pants.jpeg", "Stylish jogger pants for winter", "pants, jogger, casual", 5900, 4.5,"Male"],
    [59, "Puffer Vest", "Outerwear", "Vest", "Winter", 2022, "Nylon", "Navy", "Solid", "Casual", "Regular Fit", 80, 9500, 600, 13, "Images/puffer vest.jpeg", "Warm puffer vest for winter", "vest, puffer, casual", 5000, 4.4,"Male"],
    [60, "Faux Leather Leggings", "Bottom Wear", "Leggings", "Winter", 2023, "Faux Leather", "Black", "Solid", "Casual", "Fitted", 90, 13000, 650, 13, "Images/faux legging.jpeg", "Trendy faux leather leggings for winter", "faux leather, leggings, casual", 6000, 4.8,"Female"],
    [61, "Silk Scarves", "Accessories", "Scarves", "Spring", 2023, "Silk", "Red", "Solid", "Formal", "Long", 85, 11000, 550, 12, "Images/silk scarves.jpeg", "Elegant silk scarves for spring", "silk, scarves, formal", 5000, 4.8,"Female"],
    [62, "Tweed Blazers", "Outerwear", "Blazers", "Winter", 2023, "Tweed", "Grey", "Solid", "Formal", "Fitted", 90, 13000, 650, 13, "Images/tweed blazer.jpeg", "Chic tweed blazers for winter", "tweed, blazers, formal", 7000, 4.9,"Female"],
    [63, "Velvet Dresses", "Dress", "Dresses", "Winter", 2023, "Velvet", "Red", "Solid", "Formal", "Fitted", 85, 11000, 550, 11, "Images/velvet dresses.jpeg", "Luxurious velvet dresses for winter", "velvet, dresses, formal", 6000, 4.7,"Female"],
    [64, "Plaid Flannel Shirt", "Top Wear", "Shirt", "Fall", 2022, "Cotton", "Red", "Plaid", "Casual", "Regular Fit", 88, 12000, 750, 17, "Images/plaid flannel shirt.jpeg", "Classic plaid flannel shirt", "shirt, flannel, plaid", 6300, 4.6,"Male"],
    [65, "Polo Shirt", "Top Wear", "Shirt", "Summer", 2022, "Cotton", "Navy", "Solid", "Casual", "Regular Fit", 85, 11500, 650, 15, "Images/polo shirt.jpeg", "Classic polo shirt for summer", "shirt, polo, casual", 5800, 4.5,"Male"],
    [66, "Floral Maxi Dresses", "Dress", "Dresses", "Spring", 2023, "Cotton", "Blue", "Floral", "Feminine", "Maxi", 85, 11000, 550, 12, "Images/floral maxi dresses.jpeg", "Beautiful floral maxi dresses for spring", "floral, maxi, feminine", 6000, 4.8,"Female"],
    [67, "Quilted Jackets", "Outerwear", "Jackets", "Winter", 2023, "Polyester", "Black", "Solid", "Casual", "Quilted", 90, 13000, 650, 13, "Images/quilted jackets.jpeg", "Warm quilted jackets for winter", "quilted, jackets, casual", 7000, 4.9,"Female"],
    [68, "Slouchy Beanies", "Accessories", "Hats", "Winter", 2023, "Wool", "Grey", "Solid", "Casual", "Slouchy", 75, 9000, 400, 9, "Images/slouchy beanies.jpeg", "Cozy slouchy beanies for winter", "beanies, hats, casual", 4000, 4.5,"Female"],
    [69, "Off-Shoulder Dresses", "Dress", "Dresses", "Summer", 2023, "Cotton", "White", "Solid", "Feminine", "Off-Shoulder", 85, 11000, 550, 11, "Images/off shoulder dresses.jpeg", "Chic off-shoulder dresses for summer", "off-shoulder, dresses, feminine", 5000, 4.7,"Female"],
    [70, "Hiking Boots", "Footwear", "Boots", "Fall", 2022, "Leather", "Brown", "Solid", "Sporty", "Ankle", 80, 10000, 500, 10, "Images/hiking boots.jpeg", "Durable hiking boots for fall", "hiking, boots, sporty", 4500, 4.6,"Male"],
    [71, "Knitted Cardigans", "Outerwear", "Cardigans", "Winter", 2023, "Wool", "Beige", "Solid", "Casual", "Loose Fit", 90, 13000, 650, 13, "Images/knitted cardigans.jpeg", "Warm knitted cardigans for winter", "knitted, cardigans, casual", 7000, 4.9,"Female"],
    [72, "Bell Sleeve Tops", "Top Wear", "Tops", "Spring", 2023, "Cotton", "Pink", "Solid", "Feminine", "Bell Sleeve", 85, 11000, 550, 12, "Images/bell sleeves.jpeg", "Trendy bell sleeve tops for spring", "bell sleeve, tops, feminine", 5000, 4.8,"Female"],
    [73, "Utility Chic", "Top Wear", "Jackets", "Spring", 2023, "Cotton", "Khaki", "Solid", "Casual", "Oversized", 80, 10000, 500, 10, "Images/utility chic.jpeg", "Functional and stylish utility chic jackets for spring", "utility chic, jackets, spring",4600,3.8,"Female"],
    [74, "Asymmetrical Dresses", "Dress", "Dresses", "Summer", 2023, "Silk", "Red", "Floral", "Feminine", "Asymmetrical", 85, 11000, 550, 11, "Images/asymmetric dresses.jpeg", "Elegant and eye-catching asymmetrical dresses for summer", "asymmetrical, dresses, summer",5000,4.2,"Female"],
    [75, "Cropped Pants", "Bottom Wear", "Pants", "Fall", 2022, "Denim", "Blue", "Solid", "Casual", "Cropped", 75, 9000, 400, 9, "Images/cropped pants.jpeg", "Trendy and comfortable cropped pants for fall", "cropped, pants, denim",5500,4.8,"Female"],
    [76, "Ruffled Blouses", "Top Wear", "Blouses", "Spring", 2022, "Cotton", "White", "Floral", "Feminine", "Ruffled", 80, 10000, 500, 10, "Images/ruffled blouses.jpeg", "Whimsical and romantic ruffled blouses for spring", "ruffles, blouses, spring",5600,4.1,"Female"],
    [77, "Biker Shorts", "Bottom Wear", "Shorts", "Summer", 2023, "Polyester", "Black", "Solid", "Sporty", "Fitted", 90, 12000, 600, 12, "Images/biker shorts.jpeg", "Comfortable and stylish biker shorts for summer", "biker, shorts, summer",6000,4.4,"Female"],
    [78, "Puff Sleeves", "Top Wear", "Tops", "Fall", 2022, "Cotton", "Yellow", "Solid", "Casual", "Puff Sleeves", 70, 8000, 300, 8, "Images/puff sleeves.jpeg", "Trendy and cozy puff sleeves for fall", "puff sleeves, tops, fall",7000,4.4,"Female"],
    [79, "High-Low Dresses", "Dress", "Dresses", "Spring", 2022, "Silk", "Pink", "Floral", "Feminine", "High-Low", 85, 11000, 550, 11, "Images/high low dresses.jpeg", "Elegant and stylish high-low dresses for spring", "high-low, dresses, spring",6000,3.9,"Female"],
    [80, "Corduroy Jackets", "Outerwear", "Jackets", "Fall", 2022, "Corduroy", "Brown", "Solid", "Casual", "Fitted", 75, 9000, 400, 9, "Images/coordrey jacket.jpeg", "Cozy and stylish corduroy jackets for fall", "corduroy, jackets, fall",6000,4.3,"Male"],
    [81, "Khaki Shorts", "Bottom Wear", "Shorts", "Summer", 2022, "Cotton", "Khaki", "Solid", "Casual", "Regular Fit", 87, 12500, 800, 18, "Images/khaki shorts.jpeg", "Comfortable khaki shorts for summer", "shorts, khaki, casual", 6700, 4.7,"Male"],
    [82, "Trench Coat", "Outerwear", "Coat", "Spring", 2022, "Cotton", "Beige", "Solid", "Formal", "Regular Fit", 92, 15000, 900, 20, "Images/trench coat.jpeg", "Stylish trench coat for spring", "coat, trench, formal", 7200, 4.8,"Male"],
    [83, "Cardigan Sweater", "Top Wear", "Sweater", "Winter", 2022, "Wool", "Gray", "Solid", "Casual", "Regular Fit", 80, 10000, 600, 12, "Images/cardigan sweater.jpeg", "Warm cardigan sweater for winter", "sweater, cardigan, casual", 5200, 4.5,"Male"],
    [84, "Slim Fit Suit", "Formal Wear", "Suit", "Fall", 2022, "Wool", "Black", "Solid", "Formal", "Slim Fit", 95, 20000, 1000, 30, "Images/slim fit suit.jpeg", "Elegant slim fit suit for formal occasions", "suit, slim fit, formal", 8200, 4.9,"Male"],
    [85, "Leather Jacket", "Outerwear", "Jacket", "Winter", 2022, "Leather", "Brown", "Solid", "Casual", "Regular Fit", 89, 16000, 850, 22, "Images/leather jacket.jpeg", "Classic leather jacket for winter", "jacket, leather, casual", 7000, 4.8,"Male"],
    [86, "Crew Neck Sweater", "Top Wear", "Sweater", "Fall", 2022, "Cotton", "Blue", "Solid", "Casual", "Regular Fit", 84, 11000, 700, 14, "Images/crew neck sweater.jpeg", "Comfortable crew neck sweater for fall", "sweater, crew neck, casual", 5900, 4.6,"Male"],
    [87, "Tapered Jeans", "Bottom Wear", "Jeans", "Spring", 2022, "Denim", "Dark Blue", "Solid", "Casual", "Tapered Fit", 88, 13000, 750, 19, "Images/tapered jeans.jpeg", "Stylish tapered jeans for spring", "jeans, tapered, denim", 6300, 4.7,"Male"],
    [88, "Oversized Hoodie", "Top Wear", "Hoodie", "Winter", 2022, "Cotton", "Black", "Solid", "Casual", "Oversized Fit", 85, 14000, 800, 21, "Images/oversized hoodie.jpeg", "Comfortable oversized hoodie for winter", "hoodie, oversized, casual", 6800, 4.8,"Male"],
    [89, "Chambray Shirt", "Top Wear", "Shirt", "Spring", 2022, "Chambray", "Light Blue", "Solid", "Casual", "Regular Fit", 86, 11500, 650, 16, "Images/chambray shirt.jpeg", "Lightweight chambray shirt for spring", "shirt, chambray, casual", 5800, 4.5,"Male"],
    [90, "Utility Vest", "Outerwear", "Vest", "Fall", 2022, "Polyester", "Olive", "Solid", "Casual", "Regular Fit", 82, 10000, 600, 12, "Images/utility vest.jpeg", "Practical utility vest for fall", "vest, utility, casual", 5200, 4.4,"Male"],
    [91, "Slim Fit Dress Pants", "Formal Wear", "Pants", "Summer", 2022, "Wool", "Gray", "Solid", "Formal", "Slim Fit", 90, 13500, 750,17, "Images/slim fit dress pants.jpeg", "Elegant slim fit dress pants for formal occasions", "pants, dress, formal", 6300, 4.7,"Male"],
    [92, "Oxford Shirt", "Top Wear", "Shirt", "Fall", 2022, "Cotton", "White", "Solid", "Formal", "Regular Fit", 88, 12000, 700, 17, "Images/oxford shirt.jpeg", "Classic oxford shirt for formal wear", "shirt, oxford, formal", 6000, 4.6,"Male"],
    [93, "Quilted Jacket", "Outerwear", "Jacket", "Winter", 2022, "Polyester", "Navy", "Solid", "Casual", "Regular Fit", 84, 11000, 650, 15, "Images/quilted jacket.jpeg", "Warm quilted jacket for winter", "jacket, quilted, casual", 5700, 4.5,"Male"],
    [94, "Athletic Shorts", "Sportswear", "Shorts", "Summer", 2022, "Polyester", "Black", "Solid", "Sportswear", "Regular Fit", 85, 13000, 750, 18, "Images/atheletic shorts.jpeg", "Comfortable athletic shorts for summer", "shorts, athletic, sportswear", 6200, 4.6,"Male"],
    [95, "Sweatpants", "Bottom Wear", "Pants", "Winter", 2022, "Cotton", "Gray", "Solid", "Casual", "Regular Fit", 83, 10500, 650, 13, "Images/sweatpants.jpeg", "Cozy sweatpants for winter", "pants, sweat, casual", 5400, 4.4,"Male"],
    [96, "V-Neck Sweater", "Top Wear", "Sweater", "Fall", 2022, "Cotton", "Maroon", "Solid", "Casual", "Regular Fit", 86, 11500, 700, 16, "Images/v-neck sweater.jpeg", "Comfortable v-neck sweater for fall", "sweater, v-neck, casual", 5800, 4.5,"Male"],
    [97, "Hiking Boots", "Footwear", "Boots", "Fall", 2022, "Leather", "Brown", "Solid", "Casual", "Regular Fit", 90, 15000, 800, 20, "Images/hiking bootss.jpeg", "Durable hiking boots for outdoor adventures", "boots, hiking, casual", 7000, 4.7,"Male"],
    [98, "Chelsea Boots", "Footwear", "Boots", "Winter", 2022, "Leather", "Black", "Solid", "Casual", "Regular Fit", 92, 16000, 850, 22, "Images/chelsea boots.jpeg", "Stylish chelsea boots for winter", "boots, chelsea, casual", 7200, 4.8,"Male"],
    [99, "Track Jacket", "Sportswear", "Jacket", "Spring", 2022, "Polyester", "Blue", "Solid", "Sportswear", "Regular Fit", 85, 13000, 700, 18, "Images/track jacket.jpeg", "Lightweight track jacket for spring workouts", "jacket, track, sportswear", 6200, 4.6,"Male"],
    [100, "Polo Dress Shirt", "Formal Wear", "Shirt", "Spring", 2022, "Cotton", "Light Blue", "Solid", "Formal", "Slim Fit", 88, 12500, 750, 17, "Images/polo shirt dress.jpeg", "Elegant polo dress shirt for formal wear", "shirt, polo, formal", 6300, 4.7,"Male"],
    [101, "Leather Gloves", "Accessories", "Gloves", "Winter", 2022, "Leather", "Black", "Solid", "Formal", "Regular Fit", 86, 11000, 650, 14, "Images/leather gloves.jpeg", "Warm leather gloves for winter", "gloves, leather, formal", 5900, 4.5,"Male"],
    [102, "Puffer Jacket", "Outerwear", "Jacket", "Winter", 2022, "Nylon", "Black", "Solid", "Casual", "Regular Fit", 88, 14000, 800, 20, "Images/puffer jacket man.jpeg", "Warm puffer jacket for winter", "jacket, puffer, casual", 6700, 4.7,"Male"],
    [103, "Button Down Shirt", "Top Wear", "Shirt", "Summer", 2022, "Cotton", "White", "Solid", "Casual", "Regular Fit", 87, 12000, 700, 16, "Images/button down shirt man.jpeg", "Classic button down shirt for summer", "shirt, button down, casual", 6100, 4.6,"Male"],
    [104, "Wool Overcoat", "Outerwear", "Coat", "Winter", 2022, "Wool", "Gray", "Solid", "Formal", "Regular Fit", 93, 17000, 900, 25, "Images/wool overcoat.jpeg", "Elegant wool overcoat for winter", "coat, wool, formal", 7500, 4.8,"Male"],
    [105, "Sweater Vest", "Top Wear", "Vest", "Fall", 2022, "Cotton", "Navy", "Solid", "Casual", "Regular Fit", 82, 10000, 600, 12, "Images/sweater vest.jpeg", "Classic sweater vest for fall", "vest, sweater, casual", 5200, 4.4,"Male"],
    [106, "Denim Shorts", "Bottom Wear", "Shorts", "Summer", 2022, "Denim", "Blue", "Solid", "Casual", "Regular Fit", 86, 11500, 650, 15, "Images/denim shorts men.jpeg", "Comfortable denim shorts for summer", "shorts, denim, casual", 5700, 4.5,"Male"],
    [107, "Windbreaker", "Outerwear", "Jacket", "Spring", 2022, "Nylon", "Red", "Solid", "Sportswear", "Regular Fit", 84, 12000, 700, 18, "Images/windbreaker.jpeg", "Lightweight windbreaker for spring", "jacket, windbreaker, sportswear", 6000, 4.6,"Male"],
    [108, "Athletic Hoodie", "Sportswear", "Hoodie", "Fall", 2022, "Polyester", "Gray", "Solid", "Sportswear", "Regular Fit", 85, 13000, 750, 19, "Images/athletic hoodie.jpeg", "Comfortable athletic hoodie for workouts", "hoodie, athletic, sportswear", 6200, 4.7,"Male"],
    [109, "Loafers", "Footwear", "Shoes", "Spring", 2022, "Leather", "Brown", "Solid", "Casual", "Regular Fit", 87, 12500, 700, 16, "Images/loafers.jpeg", "Stylish loafers for spring", "shoes, loafers, casual", 6100, 4.6,"Male"],
    [110, "Fleece Jacket", "Outerwear", "Jacket", "Winter", 2022, "Fleece", "Black", "Solid", "Casual", "Regular Fit", 88, 14000, 800, 20, "Images/fleece jacket.jpeg", "Warm fleece jacket for winter", "jacket, fleece, casual", 6700, 4.7,"Male"],
    [111, "Tank Top", "Top Wear", "Tank", "Summer", 2022, "Cotton", "White", "Solid", "Casual", "Regular Fit", 84, 11000, 650, 15, "Images/tank top.jpeg", "Comfortable tank top for summer", "tank, top, casual", 5700, 4.5,"Male"],
    [112, "Raincoat", "Outerwear", "Coat", "Spring", 2022, "Nylon", "Yellow", "Solid", "Casual", "Regular Fit", 82, 10000, 600, 12, "Images/raincoat.jpeg", "Lightweight raincoat for spring", "coat, rain, casual", 5200, 4.4,"Male"],
    [113, "Turtle Neck Sweater", "Top Wear", "Sweater", "Winter", 2022, "Wool", "Black", "Solid", "Casual", "Regular Fit", 90, 15000, 750, 18, "Images/turtle neck sweater.jpeg", "Warm turtle neck sweater for winter", "sweater, turtle neck, casual", 6300, 4.7,"Male"],
    [114, "Flip Flops", "Footwear", "Sandals", "Summer", 2022, "Rubber", "Black", "Solid", "Casual", "Regular Fit", 80, 10000, 600, 10, "Images/flip flops.jpeg", "Comfortable flip flops for summer", "sandals, flip flops, casual", 5000, 4.4,"Male"],
    [115, "Corduroy Pants", "Bottom Wear", "Pants", "Fall", 2022, "Corduroy", "Brown", "Solid", "Casual", "Regular Fit", 88, 13000, 750, 20, "Images/corduroy pantsjpeg.jpeg", "Stylish corduroy pants for fall", "pants, corduroy, casual", 6300, 4.7,"Male"],
    [116, "Performance T-shirt", "Top Wear", "T-shirt", "Summer", 2022, "Polyester", "Blue", "Solid", "Sportswear", "Regular Fit", 85, 12000, 700, 16, "Images/performance t-shirt.jpeg", "Lightweight performance t-shirt for workouts", "t-shirt, performance, sportswear", 5900, 4.6,"Male"],
    [117, "Board Shorts", "Bottom Wear", "Shorts", "Summer", 2022, "Polyester", "Blue", "Solid", "Casual", "Regular Fit", 87, 12500, 700, 16, "Images/board shorts.jpeg", "Comfortable board shorts for summer", "shorts, board, casual", 6100, 4.6,"Male"],
    [118, "Winter Beanie", "Accessories", "Hat", "Winter", 2022, "Wool", "Black", "Solid", "Casual", "Regular Fit", 86, 11000, 650, 14, "Images/winter beanie.jpeg", "Warm winter beanie for cold weather", "hat, beanie, casual", 5900, 4.5,"Male"],
    [119, "Running Shoes", "Footwear", "Shoes", "Summer", 2022, "Mesh", "Gray", "Solid", "Sportswear", "Regular Fit", 90, 15000, 800, 20, "Images/running_shoes.jpeg", "Lightweight running shoes for workouts", "shoes, running, sportswear", 7000, 4.7,"Male"],
    [120, "Dress Shoes", "Footwear", "Shoes", "Fall", 2022, "Leather", "Black", "Solid", "Formal", "Regular Fit", 92, 16000, 850, 22, "Images/dress_shoes.jpeg", "Elegant dress shoes for formal occasions", "shoes, dress, formal", 7200, 4.8,"Male"],
    [121, "Beanie Hat", "Accessories", "Hat", "Winter", 2022, "Wool", "Black", "Solid", "Casual", "Regular Fit", 83, 11500, 680, 12, "Images/beanie_hat.jpeg", "Warm beanie hat for winter", "hat, beanie, casual", 5300, 4.5,"Male"],
    [122, "Leather Gloves", "Accessories", "Gloves", "Winter", 2022, "Leather", "Brown", "Solid", "Formal", "Regular Fit", 88, 13000, 750, 15, "Images/leather_gloves.jpeg", "Elegant leather gloves for winter", "gloves, leather, formal", 6200, 4.7,"Male"],
    [123, "Scarf", "Accessories", "Scarf", "Winter", 2022, "Wool", "Gray", "Solid", "Casual", "Regular Fit", 86, 12000, 700, 13, "Images/scarf.jpeg", "Cozy scarf for winter", "scarf, wool, casual", 5900, 4.6,"Female"],
    [124, "Sunglasses", "Accessories", "Sunglasses", "Summer", 2022, "Plastic", "Black", "Solid", "Casual", "Regular Fit", 90, 14000, 800, 20, "Images/sunglasses.jpeg", "Stylish sunglasses for summer", "sunglasses, casual, summer", 6800, 4.8,"Female"],
    [125, "Leather Wallet", "Accessories", "Wallet", "All Seasons", 2022, "Leather", "Black", "Solid", "Formal", "Regular Fit", 92, 15000, 850, 22, "Images/leather wallet.jpeg", "Elegant leather wallet for all occasions", "wallet, leather, formal", 7200, 4.9,"Male"],
    [126, "Silk Tie", "Accessories", "Tie", "Fall", 2022, "Silk", "Red", "Solid", "Formal", "Regular Fit", 87, 12000, 700, 15, "Images/silk_tie.jpeg", "Elegant silk tie for formal occasions", "tie, silk, formal", 6000, 4.7,"Male"],
    [127, "Cufflinks", "Accessories", "Cufflinks", "All Seasons", 2022, "Metal", "Silver", "Solid", "Formal", "Regular Fit", 88, 13000, 750, 18, "Images/cufflinks.jpeg", "Stylish cufflinks for formal occasions", "cufflinks, metal, formal", 6500, 4.8,"Male"],
    [128, "Leather Bracelet", "Accessories", "Bracelet", "Summer", 2022, "Leather", "Brown", "Solid", "Casual", "Regular Fit", 84, 11000, 650, 14, "Images/leather_bracelet.jpeg", "Trendy leather bracelet for summer", "bracelet, leather, casual", 5800, 4.6,"Male"],
    [129, "Sports Watch", "Accessories", "Watch", "All Seasons", 2022, "Rubber", "Black", "Solid", "Sportswear", "Regular Fit", 90, 14000, 800, 20, "Images/sports_watch.jpeg", "Durable sports watch for all seasons", "watch, sports, rubber", 6800, 4.8,"Male"],
    [130, "Oxidised Jewellery", "Accessories", "Jewellery", "Spring", 2023, "Metal", "Silver", "Ornate", "Ethnic", "-", 95, 11000, 550, 11, "Images/oxidised_jewellery.jpeg", "Elegant oxidised jewellery for spring", "jewellery, oxidised, ethnic", 4500, 4.6, "Female"],
    [131, "Pendants", "Accessories", "Jewellery", "Summer", 2023, "Metal", "Gold", "Solid", "Chic", "-", 94, 10000, 500, 10, "Images/pendants.jpeg", "Stylish pendants for summer", "pendants, jewellery, chic", 4000, 4.5, "Female"],
    [132, "Scrunchies", "Accessories", "Hair Accessories", "Fall", 2022, "Fabric", "Multicolor", "Solid", "Casual", "-", 90, 8000, 300, 8, "Images/scrunchies.jpeg", "Colorful scrunchies for fall", "scrunchies, hair accessories, casual", 2500, 4.4, "Female"],
    [133, "Bow", "Accessories", "Hair Accessories", "All Seasons", 2023, "Fabric", "Red", "Solid", "Cute", "-", 94, 9000, 400, 9, "Images/bow.jpeg", "Cute bows ", "bow, hair accessories, cute", 3000, 4.5, "Female"],
    [134, "Straight Jeans", "Bottom Wear", "Jeans", "Spring", 2022, "Denim", "Blue", "Solid", "Casual", "Straight Fit", 91, 11000, 550, 11, "Images/straight_ jeans.jpeg", "Comfortable straight jeans for spring", "jeans, straight, denim", 4500, 4.6, "Female"],
    [135, "Mom Jeans", "Bottom Wear", "Jeans", "Summer", 2023, "Denim", "Light Blue", "Solid", "Casual", "Relaxed Fit", 90, 12000, 600, 12, "Images/mom jeans.jpeg", "Trendy mom jeans for summer", "jeans, mom, casual", 5000, 4.7, "Female"]

]
# Convert to DataFrame
columns = [
    'Trend ID', 'Trend Name', 'Trend Type', 'Trend Subtype', 'Season', 'Year', 'Fabric',
    'Color', 'Pattern', 'Style', 'Silhouette', 'Popularity Score', 'Search Volume',
    'Social Media Mentions', 'Influencer Endorsements', 'Image URL', 'Description',
    'Keywords', 'Sales', 'User Rating', 'Gender'
]

df = pd.DataFrame(data, columns=columns)
df = df.drop(['Trend ID', 'Image URL', 'Description', 'Keywords'], axis=1)

# Encode categorical columns
label_encoders = {}
for column in df.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    df[column] = le.fit_transform(df[column])
    label_encoders[column] = le

# Normalize numerical columns
scaler = MinMaxScaler()
df[df.columns] = scaler.fit_transform(df[df.columns])

df.head()

#Step 2: Create the GAN Architecture
import tensorflow as tf
from tensorflow.keras import layers, models

# Define the generator model
def build_generator():
    model = models.Sequential()
    model.add(layers.Dense(128, activation='relu', input_dim=100))
    model.add(layers.BatchNormalization())
    model.add(layers.Dense(256, activation='relu'))
    model.add(layers.BatchNormalization())
    model.add(layers.Dense(512, activation='relu'))
    model.add(layers.BatchNormalization())
    model.add(layers.Dense(df.shape[1], activation='tanh'))
    return model

# Define the discriminator model
def build_discriminator():
    model = models.Sequential()
    model.add(layers.Dense(512, activation='relu', input_shape=(df.shape[1],)))
    model.add(layers.Dense(256, activation='relu'))
    model.add(layers.Dense(1, activation='sigmoid'))
    return model

# Build and compile the discriminator
discriminator = build_discriminator()
discriminator.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Build the generator
generator = build_generator()

# Define the combined GAN model
gan_input = layers.Input(shape=(100,))
generated_trend = generator(gan_input)
discriminator.trainable = False
gan_output = discriminator(generated_trend)
gan = models.Model(gan_input, gan_output)
gan.compile(optimizer='adam', loss='binary_crossentropy')

gan.summary()
#Step 3: Train the GAN


def train_gan(gan, generator, discriminator, epochs, batch_size, data):
    for epoch in range(epochs):
        # Train the discriminator
        for _ in range(batch_size):
            noise = np.random.normal(0, 1, (batch_size, 100))
            generated_data = generator.predict(noise)
            real_data = data[np.random.randint(0, data.shape[0], batch_size)]

            combined_data = np.concatenate([real_data, generated_data])
            labels = np.concatenate([np.ones((batch_size, 1)), np.zeros((batch_size, 1))])

            d_loss = discriminator.train_on_batch(combined_data, labels)

        # Train the generator
        noise = np.random.normal(0, 1, (batch_size, 100))
        misleading_labels = np.ones((batch_size, 1))
        g_loss = gan.train_on_batch(noise, misleading_labels)

        if epoch % 100 == 0:
            print(f"Epoch {epoch} - D Loss: {d_loss[0]}, D Accuracy: {d_loss[1]}, G Loss: {g_loss}")

# Convert dataframe to numpy array
data = df.to_numpy()

# Train the GAN
train_gan(gan, generator, discriminator, epochs=1000, batch_size=16, data=data)

