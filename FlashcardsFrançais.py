import tkinter as tk
from tkinter import scrolledtext

# Flashcard data: list of (question, answer) pairs
flashcards = [
    ("Antithèse", "Rapprochement de deux termes qui s'opposent pour en renforcer le contraste"),
    ("Antiphrase", "Fait de dire le contraire de ce que l'on pense"),
    ("Le Chiasme", "Un chiasme est composé de deux expressions qui se suivent, mais la deuxième adopte l'ordre inverse de la première"),
    ("L'oxymore", "Fait de rapprocher deux termes dont le rapprochement est innatendu et créer une apparence contradictoire"),
    ("L'ellipse", "Retirer volontairement des éléments d'une phrase sans en modifier le sens"),
    ("L'euphémisme", "Fait d'atténuer une idée ou une réalité"),
    ("La litote", "Dire moins pour suggérer d'avantage, elle prend souvent la forme d'une formulation négative"),
    ("La comparaison", "Mise en relation à l'aide d'un mot de comparaison, de deux réalités, choses, personnes"),
    ("La métaphore", "Description d'une chose par une autre qui lui ressemble, sans outil de comparaison et qui laisse deviner une similitude"),
    ("L'animalisation", "Donner des caractéristiques animales à des objets ou des personnes"),
    ("La personnification", "Donner des caractéristiques humaines à des choses ou des animaux"),
    ("L'accumulation", "Énumération de plusieurs mots dans le but de créer un effet d'amplification"),
    ("L'anaphore", "Répétition du même terme ou de la même expression en début de phrase et à plusieurs reprises"),
    ("L'énumération", "Mot ou groupes de mots spécifiques listés"),
    ("La gradation", "Énumération croissante ou décroissante"),
    ("L'hyperbole", "Exagération"),
    ("Le pléonasme", "Renforcer une idée en lui ajoutant des compléments qui ne sont pas nécessaires"),
    ("L'aposiopèse", "Interrompre la phrase pour mieux laisser suggérer la suite"),
    ("Question rhétorique", "Question dont la réponse est connue ou suggérée par la personne qui formule l'interrogation où la réponse n'est pas attendue"),
    ("Le parallélisme", "Deux constructions de phrases identiques"),
    ("La synesthésie", "Mélange des sens"),
    ("L'assonance", "Répétition d'un son voyelle"),
    ("L'allitération", "Répétition d'un son consonne"),
    ("La paronomase", "Rapprochement de mots ayant des sens différents mais ayant des sonorités similaires"),
    ("La polyptote", "Répétition d'un même mot sous plusieurs formes grammaticales"),
    ("La métonymie", "Désigner une chose par un autre terme qui convient pour le reconnaître, il existe une relation entre l'objet et le mot utilisé"),
    ("La parabole", "Courte histoire destinée à illustrer un enseignement"),
    ("La périphrase", "Fait de remplacer un mot par sa définition ou par une expression plus longue")
]

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flashcard Pour le français")
        
        self.current_card = 0
        self.is_flipped = False
        
        # Create a frame for the card and scrollbar
        card_frame = tk.Frame(root)
        card_frame.pack(pady=50)
        
        # Create a scrollable text area for the question/answer
        self.card_text = scrolledtext.ScrolledText(card_frame, wrap=tk.WORD, font=("Arial", 18), width=40, height=10, bg="white", relief="raised")
        self.card_text.pack()

        # Initially load the first question
        self.card_text.insert(tk.END, flashcards[self.current_card][0])
        self.card_text.config(state=tk.DISABLED)  # Make text read-only

        # Button to flip the card with animation
        self.flip_button = tk.Button(root, text="Retourner la carte", command=self.animate_flip, font=("Arial", 18), width=15, height=2)
        self.flip_button.pack(pady=20)

        # Navigation buttons
        self.prev_button = tk.Button(root, text="Précédente", command=self.prev_card, font=("Arial", 14), width=10)
        self.prev_button.pack(side="left", padx=20)

        self.next_button = tk.Button(root, text="Prochaine", command=self.next_card, font=("Arial", 14), width=10)
        self.next_button.pack(side="right", padx=20)

    def animate_flip(self):
        """Animate the flip of the flashcard."""
        self.shrink_label()

    def shrink_label(self):
        """Gradually reduce label width to simulate shrinking."""
        width = self.card_text.cget("width")
        if width > 1:
            self.card_text.config(width=width - 1)
            self.root.after(10, self.shrink_label)
        else:
            self.flip_card()

    def flip_card(self):
        """Flip between question and answer and expand the label back."""
        self.card_text.config(state=tk.NORMAL)  # Make text writable during the flip
        self.card_text.delete("1.0", tk.END)  # Clear the current content
        if self.is_flipped:
            self.card_text.insert(tk.END, flashcards[self.current_card][0])  # Show question
        else:
            self.card_text.insert(tk.END, flashcards[self.current_card][1])  # Show answer
        self.card_text.config(state=tk.DISABLED)  # Make text read-only again
        self.is_flipped = not self.is_flipped
        self.expand_label()

    def expand_label(self):
        """Gradually increase label width to simulate expanding."""
        width = self.card_text.cget("width")
        if width < 40:  # Target width back to 40
            self.card_text.config(width=width + 1)
            self.root.after(10, self.expand_label)

    def next_card(self):
        """Go to the next flashcard."""
        if self.current_card < len(flashcards) - 1:
            self.current_card += 1
            self.is_flipped = False
            self.card_text.config(state=tk.NORMAL)
            self.card_text.delete("1.0", tk.END)
            self.card_text.insert(tk.END, flashcards[self.current_card][0])
            self.card_text.config(state=tk.DISABLED)

    def prev_card(self):
        """Go to the previous flashcard."""
        if self.current_card > 0:
            self.current_card -= 1
            self.is_flipped = False
            self.card_text.config(state=tk.NORMAL)
            self.card_text.delete("1.0", tk.END)
            self.card_text.insert(tk.END, flashcards[self.current_card][0])
            self.card_text.config(state=tk.DISABLED)

# Create the main application window
root = tk.Tk()
app = FlashcardApp(root)

# Run the application
root.mainloop()
