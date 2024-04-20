import flet
from flet import *
from fletcarousel import BasicAnimatedHorizontalCarousel,HintLine,AutoCycle
 
 
# FOR SAMPLE I WANT TO USE FAKE DATA > THEN IMAGE FROM INTERNET
fakedata=[
    "https://jbt-en-images.s3.ap-south-1.amazonaws.com/wp-content/uploads/2022/11/15091811/Daman-Odia-Movie.jpg",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTw6rhWQzpUq_EcIhoClsHsCrrEyz_SsF9ZzP2EyAmdfufY1ToDeTkkjVkd-dNVi_4OKf4&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT8uKCwhSmWXdgmpdzuZV7ueANjNNrvikJq6g&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSq8fqkosawsoomzHabzN214KFSSgrLLhJjIcPVQqY7dKCI3Fk4SPMudDXGcBozUFTcEGU&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTUaFk6EKmWBIen5FedCn4FhnJsIUxWdzguzw&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTsCfsQYNwCRfdXNBTTFHbZdCR_srQg1zF6ZISsm3IzaMShNO6J4jdQtsuIqMEXpPgB_YU&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQy_PhxNjcoJlBq8ACYnMoORrThEV4scv6Kxg&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQN5JQCs4mKzmODlq86tGlXrCiFLjL1q7wG8A&usqp=CAU"
]
 
def main(page:Page):
	# CREATE CAROUSEL 
	carousel = BasicAnimatedHorizontalCarousel(
		page=page,
        auto_cycle=AutoCycle(duration=2),
        expand=True,
        padding=50,
        hint_lines=HintLine(
            active_color='red',
            inactive_color='purple',
            alignment=MainAxisAlignment.CENTER,
            max_list_size=400
        ),
        # SET THE ANIMATION OF SLIDE CAROUSEL
		# THERE 2 ANIMATION
		# FADE AND SCALE
 
        animated_swicher=AnimatedSwitcher(
		transition=AnimatedSwitcherTransition.SCALE,
		duration=500,
		reverse_duration=100,
		switch_in_curve=AnimationCurve.EASE_IN,
		switch_out_curve=AnimationCurve.BOUNCE_IN,
 
		# FOR MORE DETAILS ABOUT CURVE . SEE FLUTTER DOCS
		# AND SEARCH ABOUT CURVE YOU CAN USE CUSTOME OTHER
		# CURVE
			),
		# THIS IS FOR ITEM ITEMS FOR IMAGE SLIDER CAROUSE
		  items=[
            Container(
            alignment=alignment.center,
            content=Image(
                src=i,
                # expand=True,
                width=900,
                height=400,
                fit="cover"
                )
            )for i in fakedata
        ],
 
 
		)
 
	page.add(
		Column([
		Text("sample CAROUSEL ADVANCE",size=30),
			])
 
		)
	page.add(carousel)
flet.app(target=main)