import tkinter
import tkinter.messagebox 

class Feedbacker: 
    # __init__ schenken wir uns, weil nix zu tun
    
    # Standard-Implementierung macht nichts -> abstrakte Methode 
    def positive(self):
        pass

    # Standard-Implementierung macht nichts -> abstrakte Methode 
    def negative(self):
        pass

class PrintFeedbacker(Feedbacker):
    def positive(self):
        print("Richtig beantwortet")
    
    def negative(self):
        print("Falsch beantwortet, probier's nochmal")

class TkinterFeedbacker(Feedbacker):
    def positive(self):
        tkinter.messagebox.showinfo("THI SWD", "Richtig beantwortet")
    
    def negative(self):
        tkinter.messagebox.showerror("THI SWD", "Falsch beantwortet")

if __name__ == "__main__":
    if input("Nutze Tkinter? (j|n)") == "j":
        feedbacker: Feedbacker = TkinterFeedbacker()
    else:
        feedbacker: Feedbacker = PrintFeedbacker()
    # Ich hab keine Ahnung ob Feedbacker print oder Tkinter ist 

    feedbacker.positive()
    feedbacker.negative()