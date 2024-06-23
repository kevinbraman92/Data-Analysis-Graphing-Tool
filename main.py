import subprocess
import json
import sys
from helpScreen import *

GRAPH_SETTINGS = {}
DEFAULT_GRAPH_SETTINGS = {"graph_type": "bar", "x_label": "Sample Categories", "y_label": "Values", "values": [10, 20, 30, 40, 50], "title": 'Default Graph'}
SHOW_SUMMARY_STATISTICS = True


def main_menu():
    art()
    while True:
        try:
            print("\nMAIN MENU\n")
            print("Welcome to the Data Analysis Graphing Tool! Version 0.1\n")
            print("With this tool you can enter input and the program will generate a graph of your choosing and summary statistics! Pretty cool huh?")
            print("Currently supports bar & line graphs.")
            print("\nPlease select from an option below: ")
            print("1. Generate Graph")
            print("2. Exit Program")
            print("3. Help\n")
            selection = input("Your choice: ")
            if int(selection) == 1:
                generate_graph_menu()
            elif int(selection) == 2:
                print("\nThank you for using this program! Goodbye!\n")
                sys.exit()
            elif int(selection) == 3:
                print("")
                main_menu_help_screen()
            else:
                print("Invalid selection. Please choose a number displayed.")
        except ValueError:
            print("Invalid selection. Please choose a number displayed.")
        except KeyboardInterrupt:
            print("Keyboard interrupt detected, force closing program.")
            sys.exit()


def generate_graph_menu():
    while True:
        try:
            print("\nGENERATE GRAPH MENU")
            print("\nThis menu displays options for generating a graph. If you are a new user or feeling overwhelmed please check out the help screen first for guidance.")
            print("For custom graphs, select option 1. To see the program in action quickly, select option 2. If you wish to return to the main menu, selection option 3. For help, select option 4.")
            print("\nPlease select from an option below: ")
            print("1. Create Graph with Custom Data")
            print("2. Generate a Quick Graph")
            print("3. Return to Main Menu")
            print("4. Help\n")
            selection = input("Your choice: ")
            if int(selection) == 1:
                create_graph_with_custom_data_menu()
            elif int(selection) == 2:
                generate_quick_graph()
            elif int(selection) == 3:
                print("\nReturning to 'MAIN MENU'...\n")
                break
            elif int(selection) == 4:
                print("")
                generate_graph_help_screen()
            else:
                print("Invalid selection. Please choose a number displayed.")
        except ValueError:
            print("Invalid selection. Please choose a number displayed.")
        except KeyboardInterrupt:
            print("Keyboard interrupt detected, force closing program.")
            sys.exit()


def generate_quick_graph():
    global GRAPH_SETTINGS
    while True:
        try:
            print("\nGENERATE QUICK GRAPH MENU")
            print("\nChoose an option below to generate a graph based on default or random values. Default will use the hard coded predefined values, while random will generate a completely random graph.")
            print("\nPlease select from an option below: ")
            print("1. Generate Graph with Default Values")
            print("2. Generate Graph with Random Values")
            print("3. Return to Previous Menu")
            print("4. Help\n")
            selection = input("Your choice: ")
            if int(selection) == 1:
                GRAPH_SETTINGS = DEFAULT_GRAPH_SETTINGS.copy()
                output_graph()
            elif int(selection) == 2:
                print("\nGenerating random graph...")
                random_configuration()
                output_graph()
            elif int(selection) == 3:
                print("\nReturning to 'GENERATE GRAPH' menu...")
                break
            elif int(selection) == 4:
                print("")
                generate_quick_graph_help_screen()
            else:
                print("Invalid selection. Please choose a number displayed.")
        except ValueError:
            print("Invalid selection. Please choose a number displayed.")
        except KeyboardInterrupt:
            print("Keyboard interrupt detected, force closing program.")
            sys.exit()


def random_configuration():
    global GRAPH_SETTINGS
    result = subprocess.run(['python', 'randomConfigurationMicroservice.py'], stdout=subprocess.PIPE, text=True)
    GRAPH_SETTINGS = json.loads(result.stdout)


def create_graph_with_custom_data_menu():
    while True:
        try:
            print("\nGENERATE GRAPH WITH CUSTOM DATA MENU")
            print("\nThis menu displays selections for generating a custom graph. This type of graph generation is recommended for more experienced users because of the setup time.")
            print("If you would rather just quickly generate a graph, return to the previous menu and select ‘Generate a Quick Graph’.")
            print("\nPlease select from an option below: ")
            print("1. Display Current Graph Settings")
            print("2. Graph Input & Settings")
            print("3. Generate Custom Graph")
            print("4. Return to Previous Menu")
            print("5. Help\n")
            selection = input("Your choice: ")
            if int(selection) == 1:
                display_current_graph_settings()
            elif int(selection) == 2:
                graph_input_settings()
            elif int(selection) == 3:
                output_graph()
            elif int(selection) == 4:
                print("\nReturning to 'GENERATE GRAPH' menu...")
                break
            elif int(selection) == 5:
                print("")
                create_graph_with_custom_data_help_screen()
            else:
                print("Invalid selection. Please choose a number displayed.")
        except ValueError:
            print("Invalid selection. Please choose a number displayed.")
        except KeyboardInterrupt:
            print("Keyboard interrupt detected, force closing program.")
            sys.exit()


def display_current_graph_settings():
    print("\nDisplaying current graph settings...\n")
    if GRAPH_SETTINGS:
        print("Graph Type:       ", GRAPH_SETTINGS.get('graph_type', 'Not set'))
        print("Graph Title:      ", GRAPH_SETTINGS.get('title', 'Not set'))
        print("X-axis Label:     ", GRAPH_SETTINGS.get('x_label', 'Not set'))
        print("Y-axis Label:     ", GRAPH_SETTINGS.get('y_label', 'Not set'))
        print("Graph Values:     ", GRAPH_SETTINGS.get('values', 'Not set'))
    else:
        print("No graph settings are set.")

    print("\nSummary Statistics Toggle:", "Enabled" if SHOW_SUMMARY_STATISTICS else "Disabled")


def graph_input_settings():
    global GRAPH_SETTINGS
    global SHOW_SUMMARY_STATISTICS
    while True:
        try:
            print("\nGRAPH INPUT & SETTINGS MENU")
            print("\nDisplaying customization options for your graph. Check out the help option for detailed descriptions for each selection.")
            print("If at any point you want to reset to the default options, select the ‘Reset to Default Values’ option.")
            print("To generate your graph, please first make sure your data values are entered, then return to the previous menu and choose option ‘Generate Custom Graph’.")
            print("\nPlease select from an option below: ")
            print("1. Display Current Graph Settings")
            print("2. Choose Graph Type")
            print("3. Enter Graph Title")
            print("4. Enter Axis Labels")
            print("5. Enter Graph Values")
            print("6. Toggle Summary Statistics")
            print("7. Reset to Default Values")
            print("8. Return to Previous Menu")
            print("9. Help\n")
            selection = input("Your choice: ")
            if int(selection) == 1:
                display_current_graph_settings()
            elif int(selection) == 2:
                graph_types = ['bar', 'line']
                GRAPH_SETTINGS['graph_type'] = ""
                while True:
                    GRAPH_SETTINGS['graph_type'] = input("Enter graph type ('Bar' or 'Line'): ".lower())
                    if GRAPH_SETTINGS['graph_type'] not in graph_types:
                        print("Invalid graph type, please enter 'Bar' or 'Line'")
                    if GRAPH_SETTINGS['graph_type'] in graph_types:
                        break
            elif int(selection) == 3:
                GRAPH_SETTINGS['title'] = input("Enter graph title: ")
            elif int(selection) == 4:
                GRAPH_SETTINGS['x_label'] = input("Enter x-axis label: ")
                GRAPH_SETTINGS['y_label'] = input("Enter y-axis label: ")
            elif int(selection) == 5:
                while True:
                    values = input("Enter graph values separated by commas. EXAMPLE (1,2,3,4,5): ")
                    try:
                        GRAPH_SETTINGS['values'] = list(map(int, values.split(',')))
                        break
                    except ValueError:
                        print("Problem with your values. Please make sure to enter only numbers separated by commas EXAMPLE (1,2,3,4,5).")
            elif int(selection) == 6:
                if SHOW_SUMMARY_STATISTICS:
                    print("\nTOGGLING SUMMARY STATISTICS OFF...")
                    SHOW_SUMMARY_STATISTICS = False
                else:
                    print("\nTOGGLING SUMMARY STATISTICS ON...")
                    SHOW_SUMMARY_STATISTICS = True
            elif int(selection) == 7:
                print("\nResetting graph to default values...")
                GRAPH_SETTINGS = DEFAULT_GRAPH_SETTINGS.copy()
            elif int(selection) == 8:
                print("\nReturning to 'CREATE GRAPH WITH CUSTOM DATA' menu...")
                break
            elif int(selection) == 9:
                graph_input_settings_help_menu()
            else:
                print("Invalid selection. Please choose a number displayed.")
        except ValueError:
            print("Invalid selection. Please choose a number displayed.")
        except KeyboardInterrupt:
            print("Keyboard interrupt detected, force closing program.")
            sys.exit()


def output_graph():
    print("\nOUTPUTTING GRAPH...")
    settings_input = json.dumps(GRAPH_SETTINGS)
    subprocess.run(['python', 'graphMicroservice.py', settings_input])
    if SHOW_SUMMARY_STATISTICS:
        print("\nOUTPUTTING SUMMARY STATISTICS...\n")
        values_input = json.dumps(GRAPH_SETTINGS['values'])
        subprocess.run(['python', 'statsMicroservice.py', values_input])


def main():
    main_menu()


if __name__ == "__main__":
    main()
