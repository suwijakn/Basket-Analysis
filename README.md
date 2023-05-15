# This repo is for hosting my DEMO for Market Basket Analysis using streamlit

# How Association Rules Work ? 🤓

ทำความเข้าใจ Market Basket Analysis อย่างง่ายกัน   🛒 🎯
How Association Rules Can Boost Your Business

ถ้าหากเรามีข้อมูลว่าปกติแล้ว ลูกค้า ส่วนใหญ่จะซื้อ ขนมปัง คู่กับ นมสด และเรามั่นใจมากพอ (confidence) เราจะสามารถสร้าง Association Rule ดังนี้ ลูกค้าจะซื้อ ขนมปัง คู่กับ นม (Frequently Bought Together)

🧍🏻🍞   🔜   🥛

กฎเกณฑ์ที่เราสร้างขึ้นมานั้นเราสามารถนำไปใช้ประโยชน์ทางด้าน Marketing ได้อย่างหลากหลาย เช่น  “Complementary Products” “Targeted Marketing Campaigns” รวมถึงการทำ “Upselling and Cross-selling”

How Association Rules Work ? 🤓
เพื่อน ๆ ลองจินตนาการว่าเราเป็นเจ้าของร้านขายเสื้อผ้า และมีข้อมูลยอดขายจาก  POS (สมมุติเล่น ๆ นะครับ ^^) ดังนี้

Transaction 1 -> jacket, t-shirt, jeans, shoes
Transaction 2 -> dress, shoes
Transaction 3 -> jacket, scarf
Transaction 4 -> t-shirt, sunglasses, hat
Transaction 5 -> dress, jacket, shoes
Transaction 6 -> jeans, jacket, shoes

สมมุติเราอยากรู้ว่า ถ้าลูกค้าซื้อ jacket เราควรจะแนะนำอะไร หรือทำโปรอย่างไรดี ?

เริ่มกันที่ jacket และ shoes  🧥👟

ราสามารถคำนวณค่าความมั่นใจ  (confidence) ของการจับคู่ครั้งนี้ได้เท่ากับ 75% (3/4) เพราะว่า มี 4 Transaction ที่มี jacket ในรายการ และ 3 จาก 4 Transaction นั้นก็มี shoes อยู่คู่กันด้วย

จากนั้นเราลองจับคู่ jacket กับสินค้าอื่นดู และเทียบหาคู่ที่ได้ค่า confidence สูงสุด

นอกเหนือจากค่า confidence ยังมีค่าอื่น ๆ ที่นิยมนำมาใช้ประกอบการตัดสินใจด้วย เช่น support และ lift

เพื่อน ๆ สามารถศึกษาเพิ่มเติมได้โดยการ Search คีย์เวิร์ด “Basket Analysis” ซึ่งผมคิดว่าเพื่อน ๆ สามารถนำไปต่อยอดด้วยตัวเองได้ไม่ว่าจะใช้เครื่องมือทั่ว ๆ ไป เช่น Microsoft Excel ไปจนถึงการใช้ R หรือ Python

สำหรับเพื่อน ๆ ที่อยากลองเล่น Demo 🚀 ที่ผมลองทำขึ้นมาผ่านเวปไซต์ streamlit พร้อมทั้งอ่านบทความฉบับเต็มสามารถลองเข้าไปเล่นได้ที่ลิงค์ด้านล่างครับผม 🔗👇🏻

https://suwijakn-basket-analysis-basketanalysis-vc71l5.streamlit.app/

https://github.com/suwijakn/Basket-Analysis/assets/89919096/fb763a20-42f3-47eb-8b59-bf5d26b52055
