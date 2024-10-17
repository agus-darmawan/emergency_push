from api_handler import APIHandler
from serial_communication import SerialCommunication
from gui import TelelabGUI

def main():
    gui = TelelabGUI()
    api_handler = APIHandler("http://localhost")
    serial_com = SerialCommunication(com1_port="/dev/ttyS0", com2_port="/dev/ttyS1")

    nrp, password = gui.show_login()

    login_data = api_handler.login(nrp, password)
    if not login_data or 'user_id' not in login_data:
        gui.display_message("Login failed. Unable to proceed.")
        return

    user_id = login_data['user_id']
    selected_module = gui.show_module_selection()

    input_data = api_handler.get_input(selected_module, user_id)
    if input_data and 'data' in input_data:
        serial_com.send_to_com1(input_data['data'])

        output_data = serial_com.receive_from_com2()
        if output_data:
            api_handler.send_output(selected_module, output_data, user_id)
            gui.display_message(f"Module {selected_module} processed successfully!")
        else:
            gui.display_message("Failed to receive output from COM2.")
    else:
        gui.display_message("Failed to get input data from API.")

if __name__ == "__main__":
    main()