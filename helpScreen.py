def art():
    art = """
  _____        _                               _           _        _____                 _               
 |  __ \\      | |            /\\               | |         (_)      / ____|               | |              
 | |  | | __ _| |_ __ _     /  \\   _ __   __ _| |_   _ ___ _ ___  | |  __ _ __ __ _ _ __ | |__   ___ _ __ 
 | |  | |/ _` | __/ _` |   / /\\ \\ | '_ \\ / _` | | | | / __| / __| | | |_ | '__/ _` | '_ \\| '_ \\ / _ \\ '__|
 | |__| | (_| | || (_| |  / ____ \\| | | | (_| | | |_| \\__ \\ \\__ \\ | |__| | | | (_| | |_) | | | |  __/ |   
 |_____/ \\__,_|\\__\\__,_| /_/    \\_\\_| |_|\\__,_|_|\\__, |___/_|___/  \\_____|_|  \\__,_| .__/|_| |_|\\___|_|   
                                                  __/ |                            | |                    
                                                 |___/                             |_|                    

"""
    print(art)


def main_menu_help_screen():
    print("Displaying help descriptions for ‘MAIN MENU’ options...\n")
    print("Option 1: Generate Graph:\n")
    print("Select this to enter the graph generation menu. This is programs main functionality.\n")

    print("Option 2: Exit Program:\n")
    print("Select this to exit the program gracefully.\n")

    print("Option 3: Help:\n")
    print("Select this to display detailed descriptions of all available options. Each menu will have a help screen dedicated to it so don’t be afraid to consult it.")


def generate_graph_help_screen():
    print("Displaying help descriptions for ‘GENERATE GRAPH’ options...\n")
    print("Option 1: Create Graph with Custom Data:\n")
    print("This option allows you generate a graph using custom data.")
    print("Choose this if you have some experience with statistics and want to generate custom output. Has the greatest set up time.\n")

    print("Option 2: Generate a Quick Graph:\n")
    print("This option allows you to quickly generate a graph with no data needed. Select this option if you are inexperienced with graphs or statistics. No set up required.\n")

    print("Option 3: Return to Main Menu:\n")
    print("This option returns you to the main menu.\n")

    print("Option 4: Help:\n")
    print("This option displays this detailed help message.")


def create_graph_with_custom_data_help_screen():
    print("Displaying help descriptions for options for “CREATE GRAPH WITH CUSTOM DATA”...\n")
    print("Option 1: Display Current Graph Settings:\n")
    print("This option will display the current settings for the graph you are creating. By default, they will show the predefined values set at program launch.\n")

    print("Option 2: Graph Input & Settings:\n")
    print("This option will take you to a menu to customize various aspects of the graph.\n")

    print("Option 3: Generate Custom Graph:\n")
    print("This option will generate the graph based on your selections.\n")

    print("Option 4: Return to Previous Menu:\n")
    print("This option will return you to the previous “Generate Graph” menu.\n")

    print("Option 5: Help:\n")
    print("This option displays this help text.")


def generate_quick_graph_help_screen():
    print("Displaying help descriptions for ‘GENERATE QUICK GRAPH’ options...\n")
    print("Option 1: Generate a Graph with Default Values:\n")
    print("This generates a simple graph with the predefined hard-coded values, set for a bar graph.\n")

    print("Option 2: Generate Graph with Random Values:\n")
    print("This will generate a graph with completely random features, including the type of graph.\n")

    print("Option 3: Return to Previous Menu:\n")
    print("This option returns you to the 'Generate Graph' menu.\n")

    print("Option 4: Help:\n")
    print("This option displays this detailed help message.")


def graph_input_settings_help_menu():
    print("\nDisplaying help descriptions for options for “GRAPH INPUT & SETTINGS”...\n")
    print("Option 1: Generate a Graph with Default Values:\n")
    print("This option will display the current settings for the graph you are creating. By default, they will show the predefined values set at program launch.\n")

    print("Option 2: Choose Graph Type:\n")
    print("This option will allow you to select a graph type. Currently supported graphs include 'line' & 'bar' graphs.\n")

    print("Option 3: Enter Graph Title:\n")
    print("This option will allow you to enter a title for your graph.\n")

    print("Option 4: Enter Axis Labels:\n")
    print("This option will allow you to enter the X & Y Axis labels for your graph.\n")

    print("Option 5: Enter Values:\n")
    print("This option will allow you to enter the values from which the graph will be made from.\n")

    print("Option 6: Show Summary Statistics Toggle:\n")
    print("This option will toggle whether to output summary statistics. This means showing the mean, medium, and mode of your entered values.\n")

    print("Option 7: Reset to Default Values:\n")
    print("This option will reset all values to default. Use this as a ‘reset’ button to quickly reset graph settings.\n")

    print("Option 8: Return to Graph Generation Menu:\n")
    print("This option will return you to the previous ‘Graph Generation Menu’.\n")

    print("Option 9: Help:\n")
    print("This option displays this text help screen.")
