""" 
    This program is for simulating the outputs and premise of the research entitled 
    'DESIGNING AN ADAPTIVE PROGRAMMING APPROACH APPLIED IN  CLICKBAIT FILTERING IN SOCIAL MEDIA' 
"""

import tkinter as tk
import customtkinter as ctk

class InputFrame(ctk.CTkFrame):
    """
    Summary:
        The Input Frame that will serve as the typing area for user input.
    """
    def __init__(self, master, *args, **kwargs) -> None:
        super().__init__(master, *args, **kwargs)
        self.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Pack label and button side-by-side in a container frame
        container_frame = ctk.CTkFrame(self,fg_color="#87CEEB")  # Create a container for consistent layout
        container_frame.pack(fill=tk.X)  # Expand container horizontally

        self.input_label = ctk.CTkLabel(container_frame, text="Input:",
                                         font=("Arial", 17, "bold"),
                                         fg_color="#87CEEB")
        self.input_label.pack(side=tk.LEFT, pady=20, padx=10)  # Pack label on the left

        self.button = ctk.CTkButton(container_frame, text="Process",
                                    font=("Arial", 17, "bold"), text_color="white", border_color="black",
                                    border_width=2, hover_color="green")  # Add text to button
        self.button.pack(side=tk.RIGHT, pady=20, padx=15)  # Pack button on the right

        # Create text box below the container
        self.editor_text = ctk.CTkTextbox(self, corner_radius=5,
                                          font=("Arial", 12), border_color="black",
                                          border_width=2)
        self.editor_text.pack(fill=tk.BOTH, expand=True, padx=15, pady=5)

class OutputFrame(ctk.CTkFrame):
    """
    Summary:
        The Output frame that will display the results of the simulations.
    """
    def __init__(self, master, *args, **kwargs) -> None:
        super().__init__(master, *args, **kwargs)
        self.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Create labels and text boxes with same formatting as input label
        self.analysis_label = ctk.CTkLabel(self, text="Sentiment & Semantic Analysis Only:",
                                         font=("Arial", 17, "bold"),
                                         fg_color="#87CEEB")
        self.analysis_label.pack(pady=20, padx=10, anchor="w")
        self.analysis_text = ctk.CTkTextbox(self, corner_radius=5,
                                          font=("Arial", 12), state="disabled", border_color="black",
                                          border_width=2)
        self.analysis_text.pack(fill=tk.BOTH, expand=True, padx=15, pady=5)

        self.memoization_label = ctk.CTkLabel(self, text="With Memoization:",
                                         font=("Arial", 17, "bold"),
                                         fg_color="#87CEEB")
        self.memoization_label.pack(pady=20, padx=10, anchor="w")
        self.memoization_text = ctk.CTkTextbox(self, corner_radius=5,
                                          font=("Arial", 12), state="disabled", border_color="black",
                                          border_width=2)
        self.memoization_text.pack(fill=tk.BOTH, expand=True, padx=15, pady=5)

        self.tabulation_label = ctk.CTkLabel(self, text="With Tabulation:",
                                         font=("Arial", 17, "bold"),
                                         fg_color="#87CEEB")
        self.tabulation_label.pack(pady=20, padx=10, anchor="w")
        self.tabulation_text = ctk.CTkTextbox(self, corner_radius=5,
                                          font=("Arial", 12), state="disabled", border_color="black",
                                          border_width=2)
        self.tabulation_text.pack(fill=tk.BOTH, expand=True, padx=15, pady=5)

class MainFrame(ctk.CTkFrame):
    """
    Summary:
        The Main Frame of the window that Contains both the input and output frame.
    """
    def __init__(self, master, *args, **kwargs) -> None:
        super().__init__(master, *args, **kwargs)
        self.pack(fill=tk.BOTH, expand=True)

        # Create input and output frames
        self.input_frame = InputFrame(self)
        self.output_frame = OutputFrame(self)

        self.input_frame.configure(fg_color="#87CEEB")
        self.output_frame.configure(fg_color="#87CEEB")

if __name__ == '__main__':
    # Create the main window
    window = ctk.CTk(fg_color="#87CEEB")
    window.title("SIMULATION")
    window.minsize(800, 600)

    # Create the main app
    main = MainFrame(window)

    # Make the window responsive
    window.rowconfigure(0, weight=1)
    window.columnconfigure(0, weight=1)

    window.mainloop()
    