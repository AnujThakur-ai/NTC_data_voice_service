import tkinter as tk


COLORS = {
    "forest": "#103E35",
    "forest_deep": "#082C26",
    "leaf": "#1D6650",
    "cream": "#F5F4ED",
    "white": "#FFFFFF",
    "ink": "#19352E",
    "muted": "#718078",
    "line": "#E7E9E1",
    "red": "#D94343",
    "gold": "#F1B942",
    "canvas": "#F7F8F4",
    "soft_green": "#E7F1E9",
}

CATEGORIES = [
    {
        "title": "All Time Data",
        "subtitle": "One-time data packs",
        "icon": "◉",
        "color": "#EAF3EC",
        "offers": [
            "1GB @ Rs 30 · 1 Day",
            "4GB @ Rs 99 · 1 Day",
            "5GB @ Rs 109 · 7 Days",
            "12GB @ Rs 199 · 7 Days",
        ],
    },
    {
        "title": "Recurring Data",
        "subtitle": "A little data, every day",
        "icon": "↻",
        "color": "#F8F0DE",
        "offers": [
            "700MB / Day @ Rs 299 · 28 Days",
            "1.5GB / Day @ Rs 599 · 28 Days",
        ],
    },
    {
        "title": "SMS Packs",
        "subtitle": "Stay close, one text away",
        "icon": "✉",
        "color": "#F8EAEA",
        "offers": [
            "200 SMS @ Rs 35 · 1 Day",
            "200 SMS @ Rs 60 · 7 Days",
            "500 SMS @ Rs 150 · 28 Days",
        ],
    },
    {
        "title": "Social & Video",
        "subtitle": "Your favourite feeds",
        "icon": "▷",
        "color": "#E9EEF8",
        "offers": [
            "Unlimited Facebook @ Rs 55 · 3 Days",
            "Unlimited YouTube @ Rs 55 · 3 Days",
        ],
    },
]


class NtcApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Namaste Nepal | NTC Packs")
        self.root.geometry("1080x790")
        self.root.minsize(800, 700)
        self.root.configure(bg=COLORS["cream"])
        self._splash_after_id = None
        self._show_splash()

    def _show_splash(self):
        self.splash = tk.Frame(self.root, bg=COLORS["forest_deep"])
        self.splash.pack(fill="both", expand=True)

        tk.Label(
            self.splash,
            text="NTC  ·  NEPAL TELECOM",
            bg=COLORS["forest_deep"],
            fg="#B7D2C3",
            font=("TkDefaultFont", 10, "bold"),
        ).pack(pady=(72, 26))

        flag = tk.Canvas(
            self.splash,
            width=76,
            height=91,
            bg=COLORS["forest_deep"],
            highlightthickness=0,
        )
        flag.pack()
        flag.create_polygon(
            12, 4, 65, 34, 12, 36, fill=COLORS["red"], outline="#F5F3E8", width=2
        )
        flag.create_polygon(
            12, 34, 68, 65, 12, 67, fill=COLORS["red"], outline="#F5F3E8", width=2
        )
        flag.create_oval(21, 17, 33, 29, fill="#F5F3E8", outline="")
        flag.create_oval(21, 45, 33, 57, fill="#F5F3E8", outline="")

        self.namaste = tk.Label(
            self.splash,
            text="Namaste",
            bg=COLORS["forest_deep"],
            fg="#FFF9E9",
            font=("TkDefaultFont", 28, "bold"),
        )
        self.namaste.pack(pady=(18, 3))
        tk.Label(
            self.splash,
            text="नमस्ते नेपाल  ·  Welcome home",
            bg=COLORS["forest_deep"],
            fg="#D5E4D9",
            font=("TkDefaultFont", 14),
        ).pack(pady=(0, 20))
        self.intro_line = tk.Label(
            self.splash,
            text="Connecting you to the things that matter.",
            bg=COLORS["forest_deep"],
            fg="#9FBBAA",
            font=("TkDefaultFont", 10),
        )
        self.intro_line.pack()

        self.progress = tk.Canvas(
            self.splash,
            width=156,
            height=4,
            bg="#315248",
            highlightthickness=0,
        )
        self.progress.pack(pady=(28, 12))
        self.progress_bar = self.progress.create_rectangle(
            0, 0, 0, 4, fill=COLORS["gold"], outline=""
        )
        skip = tk.Label(
            self.splash,
            text="Skip intro  →",
            bg=COLORS["forest_deep"],
            fg="#B7D2C3",
            cursor="hand2",
            font=("TkDefaultFont", 9, "underline"),
        )
        skip.pack()
        skip.bind("<Button-1>", lambda _event: self._show_home())
        self.splash_step = 0
        self._animate_splash()

    def _animate_splash(self):
        if not self.splash.winfo_exists():
            return
        self.splash_step += 1
        progress = min(self.splash_step / 48, 1)
        scale = 28 + round(14 * min(self.splash_step / 18, 1))
        self.namaste.configure(font=("TkDefaultFont", scale, "bold"))
        self.progress.coords(self.progress_bar, 0, 0, 156 * progress, 4)
        if self.splash_step < 48:
            self._splash_after_id = self.root.after(35, self._animate_splash)
        else:
            self._show_home()

    def _show_home(self):
        if self._splash_after_id is not None:
            self.root.after_cancel(self._splash_after_id)
            self._splash_after_id = None
        if hasattr(self, "splash") and self.splash.winfo_exists():
            self.splash.destroy()

        page = tk.Frame(self.root, bg=COLORS["cream"])
        page.pack(fill="both", expand=True)
        self._build_header(page)
        self._build_catalog(page)
        self._build_footer(page)

    def _build_header(self, parent):
        header = tk.Frame(parent, bg=COLORS["forest"])
        header.pack(fill="x")

        nav = tk.Frame(header, bg=COLORS["forest"])
        nav.pack(fill="x", padx=42, pady=(20, 0))
        brand = tk.Frame(nav, bg=COLORS["forest"])
        brand.pack(side="left")
        tk.Label(
            brand,
            text="N",
            bg=COLORS["gold"],
            fg=COLORS["forest_deep"],
            width=2,
            height=1,
            font=("TkDefaultFont", 13, "bold"),
        ).pack(side="left", padx=(0, 10))
        tk.Label(
            brand,
            text="Nepal Telecom",
            bg=COLORS["forest"],
            fg=COLORS["white"],
            font=("TkDefaultFont", 12, "bold"),
        ).pack(side="left")
        tk.Label(
            nav,
            text="A FRIENDLY PACK GUIDE",
            bg="#205246",
            fg="#D9E7DC",
            padx=12,
            pady=6,
            font=("TkDefaultFont", 8, "bold"),
        ).pack(side="right")

        hero = tk.Frame(header, bg=COLORS["forest"])
        hero.pack(fill="x", padx=42, pady=(26, 27))
        copy = tk.Frame(hero, bg=COLORS["forest"])
        copy.pack(side="left", fill="x", expand=True)
        tk.Label(
            copy,
            text="A good day starts\nwith a good connection.",
            justify="left",
            bg=COLORS["forest"],
            fg=COLORS["white"],
            font=("TkDefaultFont", 25, "bold"),
        ).pack(anchor="w")
        tk.Label(
            copy,
            text="Find your everyday data, SMS and social packs — all in one place.",
            bg=COLORS["forest"],
            fg="#D2E3D8",
            font=("TkDefaultFont", 10),
        ).pack(anchor="w", pady=(8, 0))
        welcome = tk.Frame(hero, bg="#205246", padx=18, pady=14)
        welcome.pack(side="right", padx=(18, 0))
        tk.Label(
            welcome,
            text="नमस्ते",
            bg="#205246",
            fg="#FFF9E9",
            font=("TkDefaultFont", 17, "bold"),
        ).pack(anchor="w")
        tk.Label(
            welcome,
            text="Your NTC pack guide",
            bg="#205246",
            fg="#D2E3D8",
            font=("TkDefaultFont", 9),
        ).pack(anchor="w", pady=(3, 0))
        tk.Frame(header, bg=COLORS["red"], height=4).pack(fill="x")

    def _build_catalog(self, parent):
        content = tk.Frame(parent, bg=COLORS["cream"])
        content.pack(fill="both", expand=True, padx=36, pady=(16, 6))

        toolbar = tk.Frame(content, bg=COLORS["cream"])
        toolbar.pack(fill="x", pady=(0, 11))
        titles = tk.Frame(toolbar, bg=COLORS["cream"])
        titles.pack(side="left", anchor="w")
        tk.Label(
            titles,
            text="Packages for you",
            bg=COLORS["cream"],
            fg=COLORS["ink"],
            font=("TkDefaultFont", 17, "bold"),
        ).pack(anchor="w")
        self.results_label = tk.Label(
            titles,
            text="11 packs · clear prices · no surprises",
            bg=COLORS["cream"],
            fg=COLORS["muted"],
            font=("TkDefaultFont", 9),
        )
        self.results_label.pack(anchor="w", pady=(2, 0))

        search_box = tk.Frame(
            toolbar,
            bg=COLORS["white"],
            highlightbackground=COLORS["line"],
            highlightthickness=1,
        )
        search_box.pack(side="right", padx=(10, 0), pady=2)
        tk.Label(
            search_box,
            text="⌕",
            bg=COLORS["white"],
            fg=COLORS["muted"],
            font=("TkDefaultFont", 15),
        ).pack(side="left", padx=(10, 4))
        self.search_var = tk.StringVar(value="Search packs")
        self.search_var.trace_add("write", self._filter_catalog)
        self.search_entry = tk.Entry(
            search_box,
            textvariable=self.search_var,
            width=23,
            relief="flat",
            bg=COLORS["white"],
            fg=COLORS["ink"],
            insertbackground=COLORS["ink"],
            font=("TkDefaultFont", 9),
        )
        self.search_entry.pack(side="left", ipady=9, padx=(0, 10))
        self.search_entry.configure(fg=COLORS["muted"])
        self.search_entry.bind(
            "<FocusIn>",
            lambda _event: self._clear_search_hint(),
        )
        self.search_entry.bind(
            "<FocusOut>",
            lambda _event: self._restore_search_hint(),
        )

        self.active_category = "All packs"
        self.filter_bar = tk.Frame(content, bg=COLORS["cream"])
        self.filter_bar.pack(fill="x", pady=(0, 12))
        self.filter_buttons = {}
        self._build_filter_buttons()

        catalog = tk.Frame(content, bg=COLORS["cream"])
        catalog.pack(fill="both", expand=True)
        self.catalog_canvas = tk.Canvas(
            catalog,
            bg=COLORS["canvas"],
            highlightthickness=0,
            bd=0,
        )
        scrollbar = tk.Scrollbar(
            catalog,
            orient="vertical",
            command=self.catalog_canvas.yview,
            relief="flat",
            bd=0,
            width=10,
        )
        self.catalog_canvas.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        self.catalog_canvas.pack(side="left", fill="both", expand=True)
        self.catalog_grid = tk.Frame(self.catalog_canvas, bg=COLORS["canvas"])
        self.catalog_window = self.catalog_canvas.create_window(
            (0, 0), window=self.catalog_grid, anchor="nw"
        )
        self.catalog_grid.bind(
            "<Configure>",
            lambda _event: self.catalog_canvas.configure(
                scrollregion=self.catalog_canvas.bbox("all")
            ),
        )
        self.catalog_canvas.bind(
            "<Configure>",
            lambda event: self.catalog_canvas.itemconfigure(
                self.catalog_window, width=event.width
            ),
        )
        self.catalog_canvas.bind("<MouseWheel>", self._scroll_catalog)
        self.catalog_canvas.bind("<Button-4>", self._scroll_catalog)
        self.catalog_canvas.bind("<Button-5>", self._scroll_catalog)
        self._render_catalog()

    def _build_filter_buttons(self):
        categories = [("All packs", None)] + [
            (category["title"], category) for category in CATEGORIES
        ]
        for label, category in categories:
            count = (
                sum(len(item["offers"]) for item in CATEGORIES)
                if category is None
                else len(category["offers"])
            )
            text = "{}  {}".format(label, count)
            button = tk.Button(
                self.filter_bar,
                text=text,
                relief="flat",
                bd=0,
                cursor="hand2",
                font=("TkDefaultFont", 9, "bold"),
                padx=12,
                pady=8,
                command=lambda selected=label: self._select_category(selected),
            )
            button.pack(side="left", padx=(0, 7))
            self.filter_buttons[label] = button
        self._update_filter_styles()

    def _update_filter_styles(self):
        for label, button in self.filter_buttons.items():
            active = label == self.active_category
            button.configure(
                bg=COLORS["leaf"] if active else COLORS["white"],
                fg=COLORS["white"] if active else COLORS["muted"],
                activebackground=COLORS["forest"] if active else COLORS["soft_green"],
                activeforeground=COLORS["white"] if active else COLORS["ink"],
            )

    def _select_category(self, category):
        self.active_category = category
        self._update_filter_styles()
        self._render_catalog()

    def _clear_search_hint(self):
        if self.search_entry.get() == "Search packs":
            self.search_entry.delete(0, "end")
            self.search_entry.configure(fg=COLORS["ink"])

    def _restore_search_hint(self):
        if not self.search_entry.get():
            self.search_entry.insert(0, "Search packs")
            self.search_entry.configure(fg=COLORS["muted"])

    def _filter_catalog(self, *_args):
        self._render_catalog()

    def _scroll_catalog(self, event):
        if getattr(event, "num", None) == 4:
            direction = -1
        elif getattr(event, "num", None) == 5:
            direction = 1
        else:
            direction = -1 if event.delta > 0 else 1
        self.catalog_canvas.yview_scroll(direction, "units")

    def _render_catalog(self):
        for widget in self.catalog_grid.winfo_children():
            widget.destroy()

        query = self.search_var.get().strip().lower()
        if query == "search packs":
            query = ""
        visible_offers = []
        for category in CATEGORIES:
            if self.active_category not in ("All packs", category["title"]):
                continue
            for offer in category["offers"]:
                if query and query not in "{} {}".format(
                    category["title"], offer
                ).lower():
                    continue
                visible_offers.append((category, offer))

        self.results_label.configure(
            text="{} pack{} found".format(
                len(visible_offers), "" if len(visible_offers) == 1 else "s"
            )
        )
        for column in range(2):
            self.catalog_grid.grid_columnconfigure(column, weight=1, uniform="pack")

        if not visible_offers:
            tk.Label(
                self.catalog_grid,
                text="No packs found. Try another search.",
                bg=COLORS["canvas"],
                fg=COLORS["muted"],
                font=("TkDefaultFont", 11),
                pady=38,
            ).grid(row=0, column=0, columnspan=2)
        for index, (category, offer) in enumerate(visible_offers):
            card = self._make_offer_card(self.catalog_grid, category, offer)
            card.grid(
                row=index // 2,
                column=index % 2,
                sticky="nsew",
                padx=(0, 7) if index % 2 == 0 else (7, 0),
                pady=(0, 10),
            )

        self.catalog_canvas.yview_moveto(0)

    def _make_offer_card(self, parent, category, offer):
        card = tk.Frame(
            parent,
            bg=COLORS["white"],
            highlightbackground=COLORS["line"],
            highlightthickness=1,
        )
        details, pricing = offer.split(" @ Rs ", 1)
        price, validity = pricing.split(" · ", 1)

        top = tk.Frame(card, bg=COLORS["white"])
        top.pack(fill="x", padx=15, pady=(13, 8))
        tk.Label(
            top,
            text=category["title"].upper(),
            bg=category["color"],
            fg=COLORS["leaf"],
            padx=8,
            pady=4,
            font=("TkDefaultFont", 8, "bold"),
        ).pack(side="left")
        tk.Label(
            top,
            text=validity,
            bg=COLORS["canvas"],
            fg=COLORS["muted"],
            padx=8,
            pady=4,
            font=("TkDefaultFont", 8, "bold"),
        ).pack(side="right")

        tk.Label(
            card,
            text=details,
            bg=COLORS["white"],
            fg=COLORS["ink"],
            font=("TkDefaultFont", 12, "bold"),
        ).pack(anchor="w", padx=16)
        bottom = tk.Frame(card, bg=COLORS["white"])
        bottom.pack(fill="x", padx=15, pady=(10, 13))
        tk.Label(
            bottom,
            text="Rs {}".format(price),
            bg=COLORS["white"],
            fg=COLORS["forest"],
            font=("TkDefaultFont", 17, "bold"),
        ).pack(side="left")
        tk.Button(
            bottom,
            text="Select pack  →",
            bg=COLORS["leaf"],
            fg=COLORS["white"],
            activebackground=COLORS["forest"],
            activeforeground=COLORS["white"],
            relief="flat",
            bd=0,
            cursor="hand2",
            padx=12,
            pady=7,
            font=("TkDefaultFont", 9, "bold"),
            command=lambda selected=offer: self._confirm_offer(selected),
        ).pack(side="right")

        for widget in (card, top, bottom):
            widget.bind(
                "<Enter>",
                lambda _event, target=card: target.configure(
                    highlightbackground="#AFC8B7"
                ),
            )
            widget.bind(
                "<Leave>",
                lambda _event, target=card: target.configure(
                    highlightbackground=COLORS["line"]
                ),
            )
        return card

    def _build_footer(self, parent):
        footer = tk.Frame(parent, bg=COLORS["cream"])
        footer.pack(fill="x", padx=36, pady=(0, 12))
        tk.Frame(footer, bg=COLORS["line"], height=1).pack(fill="x", pady=(0, 10))
        self.status_label = tk.Label(
            footer,
            text="Made with a Namaste  ·  Demo only — selecting a pack does not activate a service.",
            bg=COLORS["cream"],
            fg=COLORS["muted"],
            font=("TkDefaultFont", 8),
        )
        self.status_label.pack(anchor="w")

    def _confirm_offer(self, offer):
        self.status_label.configure(
            text="Selected: {}  ·  Demo only — no service was activated.".format(
                offer
            ),
            fg=COLORS["leaf"],
        )
        details, pricing = offer.split(" @ Rs ", 1)
        price, validity = pricing.split(" · ", 1)

        dialog = tk.Toplevel(self.root)
        dialog.title("Pack selected")
        dialog.configure(bg=COLORS["cream"])
        dialog.resizable(False, False)
        dialog.transient(self.root)
        dialog.geometry("440x350")
        dialog.bind("<Escape>", lambda _event: dialog.destroy())
        dialog.protocol("WM_DELETE_WINDOW", dialog.destroy)

        self.root.update_idletasks()
        x = self.root.winfo_rootx() + (self.root.winfo_width() - 440) // 2
        y = self.root.winfo_rooty() + (self.root.winfo_height() - 350) // 2
        dialog.geometry("+{}+{}".format(max(x, 0), max(y, 0)))

        tk.Frame(dialog, bg=COLORS["red"], height=5).pack(fill="x")
        body = tk.Frame(dialog, bg=COLORS["cream"], padx=26, pady=20)
        body.pack(fill="both", expand=True)
        tk.Label(
            body,
            text="✓",
            bg=COLORS["soft_green"],
            fg=COLORS["leaf"],
            width=3,
            height=1,
            font=("TkDefaultFont", 20, "bold"),
        ).pack(anchor="w", pady=(0, 12))
        tk.Label(
            body,
            text="Pack selected",
            bg=COLORS["cream"],
            fg=COLORS["ink"],
            font=("TkDefaultFont", 19, "bold"),
        ).pack(anchor="w")
        tk.Label(
            body,
            text="Your selection is ready to review.",
            bg=COLORS["cream"],
            fg=COLORS["muted"],
            font=("TkDefaultFont", 10),
        ).pack(anchor="w", pady=(4, 15))

        selected = tk.Frame(
            body,
            bg=COLORS["white"],
            highlightbackground=COLORS["line"],
            highlightthickness=1,
            padx=14,
            pady=12,
        )
        selected.pack(fill="x")
        tk.Label(
            selected,
            text=details,
            bg=COLORS["white"],
            fg=COLORS["ink"],
            font=("TkDefaultFont", 11, "bold"),
        ).pack(anchor="w")
        tk.Label(
            selected,
            text="Rs {}   ·   {}".format(price, validity),
            bg=COLORS["white"],
            fg=COLORS["leaf"],
            font=("TkDefaultFont", 10, "bold"),
        ).pack(anchor="w", pady=(5, 0))

        tk.Label(
            body,
            text="Demo only — no real package was activated.",
            bg=COLORS["cream"],
            fg=COLORS["muted"],
            font=("TkDefaultFont", 9),
        ).pack(anchor="w", pady=(13, 12))
        tk.Button(
            body,
            text="Done",
            bg=COLORS["leaf"],
            fg=COLORS["white"],
            activebackground=COLORS["forest"],
            activeforeground=COLORS["white"],
            relief="flat",
            bd=0,
            cursor="hand2",
            padx=22,
            pady=8,
            font=("TkDefaultFont", 9, "bold"),
            command=dialog.destroy,
        ).pack(anchor="e")
        dialog.grab_set()
        dialog.focus_set()


def main():
    root = tk.Tk()
    NtcApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
