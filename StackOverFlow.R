ui <- fluidPage(
		titlePanel("Show map of a given state"),
  		sidebarLayout(
    		sidebarPanel(
      		textInput("state", label = "State", value = "CA", placeholder = "California or CA"),
      		actionButton("showU","Show map")
      		),
    		mainPanel(
           		conditionalPanel(
      				condition = "input.showU > 0",
      				#showModal(urlModal("url"),"Here's the link"),
      				a(href=uiOutput("url"),"Show in Google Map",target="_blank")
      			)
    		)
		)
	)

server <- function(input, output){
	observeEvent(input$showU,{
		output$url <-renderUI({paste("https://www.google.com/maps/place/", input$state, sep="")})
	})
}

shinyApp(ui,server)