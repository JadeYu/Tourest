library(shiny)

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
                h3(textOutput("state")),
                uiOutput("url")
            )
        )
    )
)

server <- function(input, output){
    observeEvent(input$showU,{
    		state = input$state
        output$state <- renderText(paste("Map of",state, ":"))
        output$url <-renderUI({a(href=paste("https://www.google.com/maps/place/", state, sep=""),"Show in Google Map",target="_blank")})
    })
}

shinyApp(ui,server)
