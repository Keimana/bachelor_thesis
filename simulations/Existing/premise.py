""" 
This program is for simulating the outputs and premise of the research entitled 
'DESIGNING AN ADAPTIVE PROGRAMMING APPROACH APPLIED IN CLICKBAIT FILTERING IN SOCIAL MEDIA' 
"""

import tkinter as tk
import customtkinter as ctk
from analysis import SSA, SSAM, SSAT
from tagging import is_clickbait

class InputFrame(ctk.CTkFrame):
    """
    Summary:
        The Input Frame that will serve as the typing area for user input.
    """
    def __init__(self, master, *args, **kwargs) -> None:
        super().__init__(master, *args, **kwargs)
        self.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Pack label and button side-by-side in a container frame
        container_frame = ctk.CTkFrame(self, fg_color="#090B0A")  # Create a container for consistent layout
        container_frame.pack(fill=tk.X)  # Expand container horizontally

        self.input_label = ctk.CTkLabel(container_frame, text="Input:",
                                         font=("Arial", 17, "bold"),
                                         fg_color="#090B0A")
        self.input_label.pack(side=tk.LEFT, pady=5, padx=10, border_color="gray",
                                          border_width=1)  # Pack label on the left

        self.button = ctk.CTkButton(container_frame, text="Process", command=self.process_input)  # Add text to button
        self.button.pack(side=tk.RIGHT, pady=5, padx=15)  # Pack button on the right

        # Create text box below the container
        self.editor_text = ctk.CTkTextbox(self,
                                          font=("Arial", 12), border_color="gray")
        self.editor_text.pack(fill=tk.BOTH, padx=1, pady=1)

    def process_input(self):
        input_text = self.editor_text.get("1.0", "end-1c")
        if input_text:
            # Perform Semantic and Sentiment Analysis Only
            sentiment, semantics, classification = SSA(input_text)

            # Perform Semantic and Sentiment Analysis with Memoization
            sentiment_m, semantics_m, classification_m = SSAM(input_text)

            # Perform Semantic and Sentiment Analysis with Tabulation
            sentiment_t, semantics_t, classification_t = SSAT(input_text)

            # Update the text boxes in all output frames with classification results
            self.master.output_frame.analysis_text.configure(state="normal")
            self.master.output_frame.analysis_text.delete("1.0", tk.END)
            self.master.output_frame.analysis_text.insert(tk.END, "Semantic and Sentiment Analysis Only:\n")
            self.master.output_frame.analysis_text.insert(tk.END, f"Sentiment: {sentiment}\n")
            self.master.output_frame.analysis_text.insert(tk.END, f"Semantics: {semantics}\n")
            self.master.output_frame.analysis_text.insert(tk.END, f"Classification: {classification}\n\n")
            self.master.output_frame.analysis_text.configure(state="disabled")

            self.master.output_frame.memoization_text.configure(state="normal")
            self.master.output_frame.memoization_text.delete("1.0", tk.END)
            self.master.output_frame.memoization_text.insert(tk.END, "Semantic and Sentiment Analysis with Memoization:\n")
            self.master.output_frame.memoization_text.insert(tk.END, f"Sentiment: {sentiment_m}\n")
            self.master.output_frame.memoization_text.insert(tk.END, f"Semantics: {semantics_m}\n")
            self.master.output_frame.memoization_text.insert(tk.END, f"Classification: {classification_m}\n\n")
            self.master.output_frame.memoization_text.configure(state="disabled")

            self.master.output_frame.tabulation_text.configure(state="normal")
            self.master.output_frame.tabulation_text.delete("1.0", tk.END)
            self.master.output_frame.tabulation_text.insert(tk.END, "Semantic and Sentiment Analysis with Tabulation:\n")
            self.master.output_frame.tabulation_text.insert(tk.END, f"Sentiment: {sentiment_t}\n")
            self.master.output_frame.tabulation_text.insert(tk.END, f"Semantics: {semantics_t}\n")
            self.master.output_frame.tabulation_text.insert(tk.END, f"Classification: {classification_t}\n\n")
            self.master.output_frame.tabulation_text.configure(state="disabled")


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
                                         fg_color="#090B0A")
        self.analysis_label.pack(pady=10, padx=10, anchor="n")
        self.analysis_text = ctk.CTkTextbox(self, corner_radius=0,
                                          font=("Arial", 12), state="disabled", border_color="gray",
                                          border_width=1)
        self.analysis_text.pack(fill=tk.BOTH, expand=False, padx=15, pady=5)

        self.memoization_label = ctk.CTkLabel(self, text="With Memoization:",
                                         font=("Arial", 17, "bold"),
                                         fg_color="#090B0A")
        self.memoization_label.pack(pady=10, padx=10, anchor="n")
        self.memoization_text = ctk.CTkTextbox(self, corner_radius=0,
                                          font=("Arial", 12), state="disabled", border_color="gray",
                                          border_width=1)
        self.memoization_text.pack(fill=tk.BOTH, expand=False, padx=15, pady=5)

        self.tabulation_label = ctk.CTkLabel(self, text="With Tabulation:",
                                         font=("Arial", 17, "bold"),
                                         fg_color="#090B0A")
        self.tabulation_label.pack(pady=10, padx=10, anchor="n")
        self.tabulation_text = ctk.CTkTextbox(self, corner_radius=0,
                                          font=("Arial", 12), state="disabled", border_color="gray",
                                          border_width=1)
        self.tabulation_text.pack(fill=tk.BOTH, expand=False, padx=15, pady=5)

class MainFrame(ctk.CTkFrame):
    """
    Summary:
        The Main Frame of the window that Contains both the input and output frame.
    """
    def __init__(self, master, *args, **kwargs) -> None:
        super().__init__(master, *args, **kwargs)
        self.pack(fill=tk.BOTH, expand=False)

        # Create input and output frames
        self.input_frame = InputFrame(self)
        self.output_frame = OutputFrame(self)

        self.input_frame.configure(fg_color="#090B0A")
        self.output_frame.configure(fg_color="#090B0A")

if __name__ == '__main__':
    # Create the main window
    window = ctk.CTk(fg_color="#090B0A")
    window.title("SIMULATION")
    window.minsize(800, 600)

    # Create the main app
    main = MainFrame(window)

    # Make the window responsive
    window.rowconfigure(0, weight=1)
    window.columnconfigure(0, weight=1)

    window.mainloop()
