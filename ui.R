shinyUI( 
	fluidPage(
		titlePanel("Tourest: make your own day-tour plan in clicks"),
  		sidebarLayout(
    			sidebarPanel(
      			textInput("state", label = "State", value = "CA", placeholder = "California or CA"),
      			textInput("city", label = "City", value = "San Francisco", placeholder = "San Francisco"),
      			actionButton("showA","Show the most popular attractions"),
      			conditionalPanel(
      				condition = "input.showA > 0",
      				textInput("Aselection", label = "Select attractions", value = "2, 4"),
      				helpText("For example: 2, 4, 6"), 
      				textInput("dining_pref", label = "Specify dining preference", value = "Chinese", placeholder = "Chinese"),
      				helpText("You can put in: Italian, Chinese"),
      				sliderInput("radius", label = "Search radius from the selected attractions (m)", min = 500, max = 5000, value = 2000, round = TRUE, animate = TRUE),
      				actionButton("showR","Show the most popular restaurants")
      			),
      			conditionalPanel(
      				condition = "input.showR > 0",
      				textInput("Rselection", label = "Select restaurant(s)", value = "1"),
      				helpText("For example: 1, 3"),
      				textInput("start", label = "Starting point", value = "City Hall", placeholder = "City Hall"),
      				helpText("You can put in: Downtown Bart or Super 8"),
      				checkboxInput("same", "Ending point is the same", FALSE),
      				conditionalPanel(
      					condition = "!input.same",
      					textInput("end", label = "Ending point", value = "City Hall", placeholder = "City Hall")
      				),
      				actionButton("showU","Generate an optimized route")
      			),
      			helpText("Codes can be found in:", a(href="https://github.com/JadeYu/Tourest.git","GitHub",target="_blank"))     
     		),
    			mainPanel(
      			conditionalPanel(
      				condition = "input.showA == 0",
      				imageOutput("wait",width=600,height=500)
      			),
      			conditionalPanel(
      				condition = "input.showA > 0",
      				h3("Top 15 attractions in the selected city:"),
      				column(12,
      					h4(tableOutput("attractions"))
      				)
      			),
      			conditionalPanel(
      				condition = "input.showR > 0",
      				h3("Top restaurants near the selected attractions:"),
      				column(12,
      					h4(tableOutput("restaurants"))
      				)
      			),
      			conditionalPanel(
      				condition = "input.showU > 0",
      				h3("Optimized route:"),
      				column(12,
      					uiOutput("url")
      				)
      			)
    			)
		)
	)
)