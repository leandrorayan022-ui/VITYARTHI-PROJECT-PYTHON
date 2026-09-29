import random
import tkinter as tk
from tkinter import messagebox


class RockPaperScissorsApp:

  def __init__(self, root):
    self.root = root
    self.root.title("Rock Paper Scissors - Modern Edition")
    self.root.geometry("650x650")
    self.root.minsize(600, 600)
    self.root.configure(bg="#0f172a")  # Deep modern slate background

    self.target_points = 3
    self.point_ai = 0
    self.point_hi = 0
    self.game_active = False

    self.create_setup_screen()

  def clear_window(self):
    for widget in self.root.winfo_children():
      widget.destroy()

  def create_setup_screen(self):
    self.clear_window()

    container = tk.Frame(self.root, bg="#0f172a")
    container.pack(expand=True, fill="both", padx=40, pady=40)

    title_lbl = tk.Label(
        container,
        text="🎮 ROCK · PAPER · SCISSORS",
        font=("Segoe UI", 24, "bold"),
        bg="#0f172a",
        fg="#f8fafc",
    )
    title_lbl.pack(pady=(20, 10))

    subtitle_lbl = tk.Label(
        container,
        text="Enter or select the target score to win the match",
        font=("Segoe UI", 12),
        bg="#0f172a",
        fg="#94a3b8",
    )
    subtitle_lbl.pack(pady=(0, 30))

    input_frame = tk.Frame(container, bg="#1e293b", padx=20, pady=20)
    input_frame.pack(pady=10, fill="x")

    lbl = tk.Label(
        input_frame,
        text="Target Points:",
        font=("Segoe UI", 12, "bold"),
        bg="#1e293b",
        fg="#f8fafc",
    )
    lbl.pack(side="left", padx=10)

    self.score_entry = tk.Entry(
        input_frame,
        font=("Segoe UI", 14),
        width=10,
        justify="center",
        bd=0,
        highlightthickness=2,
        highlightbackground="#475569",
        highlightcolor="#3b82f6",
    )
    self.score_entry.insert(0, "3")
    self.score_entry.pack(side="left", padx=10)

    quick_frame = tk.Frame(container, bg="#0f172a")
    quick_frame.pack(pady=20)

    for pts in [3, 5, 10]:
      btn = tk.Button(
          quick_frame,
          text=f"First to {pts}",
          font=("Segoe UI", 10, "bold"),
          bg="#334155",
          fg="white",
          activebackground="#475569",
          activeforeground="white",
          bd=0,
          padx=15,
          pady=8,
          cursor="hand2",
          command=lambda p=pts: self.start_game(p),
      )
      btn.pack(side="left", padx=5)

    start_btn = tk.Button(
        container,
        text="START GAME",
        font=("Segoe UI", 12, "bold"),
        bg="#2563eb",
        fg="white",
        activebackground="#1d4ed8",
        activeforeground="white",
        bd=0,
        padx=30,
        pady=12,
        cursor="hand2",
        command=self.validate_and_start,
    )
    start_btn.pack(pady=30)

  def validate_and_start(self):
    try:
      pts = int(self.score_entry.get())
      if pts <= 0:
        raise ValueError
      self.start_game(pts)
    except ValueError:
      messagebox.showerror(
          "Invalid Input", "Please enter a valid positive integer for points!"
      )

  def start_game(self, points):
    self.target_points = points
    self.point_ai = 0
    self.point_hi = 0
    self.game_active = True
    self.create_game_screen()

  def create_game_screen(self):
    self.clear_window()

    header_frame = tk.Frame(self.root, bg="#1e293b", pady=15)
    header_frame.pack(fill="x", padx=20, pady=20)

    self.phi_label = tk.Label(
        header_frame,
        text=f"You: {self.point_hi}",
        font=("Segoe UI", 16, "bold"),
        bg="#1e293b",
        fg="#ef4444",
    )
    self.phi_label.pack(side="left", padx=30)

    target_lbl = tk.Label(
        header_frame,
        text=f"Target: {self.target_points}",
        font=("Segoe UI", 12),
        bg="#1e293b",
        fg="#94a3b8",
    )
    target_lbl.pack(side="left", expand=True)

    self.pai_label = tk.Label(
        header_frame,
        text=f"AI: {self.point_ai}",
        font=("Segoe UI", 16, "bold"),
        bg="#1e293b",
        fg="#3b82f6",
    )
    self.pai_label.pack(side="right", padx=30)

    arena_frame = tk.Frame(self.root, bg="#0f172a")
    arena_frame.pack(expand=True, fill="both", padx=20)

    ai_title = tk.Label(
        arena_frame,
        text="AI's Choice",
        font=("Segoe UI", 11),
        bg="#0f172a",
        fg="#94a3b8",
    )
    ai_title.pack(pady=(10, 0))

    self.ai_move_label = tk.Label(
        arena_frame,
        text="❓",
        font=("Segoe UI", 40),
        bg="#1e293b",
        fg="white",
        width=5,
        height=2,
    )
    self.ai_move_label.pack(pady=10)

    self.result_label = tk.Label(
        arena_frame,
        text="Make your move!",
        font=("Segoe UI", 18, "bold"),
        bg="#0f172a",
        fg="#e2e8f0",
    )
    self.result_label.pack(pady=20)

    self.controls_frame = tk.Frame(self.root, bg="#0f172a")
    self.controls_frame.pack(pady=30)

    choices = [
        ("Rock 🪨", "rock"),
        ("Paper 📄", "paper"),
        ("Scissors ✂️", "scissor"),
    ]

    for text, val in choices:
      btn = tk.Button(
          self.controls_frame,
          text=text,
          font=("Segoe UI", 14, "bold"),
          bg="#334155",
          fg="white",
          activebackground="#475569",
          activeforeground="white",
          width=12,
          pady=12,
          bd=0,
          cursor="hand2",
          command=lambda v=val: self.play_round(v),
      )
      btn.pack(side="left", padx=10)

    bottom_frame = tk.Frame(self.root, bg="#0f172a")
    bottom_frame.pack(fill="x", padx=20, pady=10)

    reset_btn = tk.Button(
        bottom_frame,
        text="← Main Menu",
        font=("Segoe UI", 10),
        bg="#475569",
        fg="white",
        bd=0,
        padx=15,
        pady=5,
        cursor="hand2",
        command=self.create_setup_screen,
    )
    reset_btn.pack(side="left")

    exit_btn = tk.Button(
        bottom_frame,
        text="Exit",
        font=("Segoe UI", 10),
        bg="#991b1b",
        fg="white",
        bd=0,
        padx=15,
        pady=5,
        cursor="hand2",
        command=self.root.destroy,
    )
    exit_btn.pack(side="right")

  def play_round(self, player_choice):
    if not self.game_active:
      return

    choices_map = {"rock": "🪨", "paper": "📄", "scissor": "✂️"}
    keys = ["rock", "paper", "scissor"]
    ai_choice = random.choice(keys)

    self.ai_move_label.config(text=choices_map[ai_choice])

    if player_choice == ai_choice:
      result = "It's a Tie!"
      color = "#e2e8f0"
    elif (
        (player_choice == "rock" and ai_choice == "scissor")
        or (player_choice == "paper" and ai_choice == "rock")
        or (player_choice == "scissor" and ai_choice == "paper")
    ):
      result = "You Win This Round! 🎉"
      color = "#ef4444"
      self.point_hi += 1
    else:
      result = "AI Wins This Round! 🤖"
      color = "#3b82f6"
      self.point_ai += 1

    self.phi_label.config(text=f"You: {self.point_hi}")
    self.pai_label.config(text=f"AI: {self.point_ai}")
    self.result_label.config(text=result, fg=color)

    if self.point_hi == self.target_points:
      self.end_match("🏆 YOU WON THE MATCH! 🏆", "#ef4444")
    elif self.point_ai == self.target_points:
      self.end_match("💀 AI WON THE MATCH! 💀", "#3b82f6")

  def end_match(self, message, color):
    self.game_active = False
    self.result_label.config(text=message, fg=color)
    for widget in self.controls_frame.winfo_children():
      widget.config(state="disabled", bg="#1e293b", fg="#64748b", cursor="")


if __name__ == "__main__":
  root = tk.Tk()
  app = RockPaperScissorsApp(root)
  root.mainloop()