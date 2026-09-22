import sys
import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def create_presentation():
    prs = Presentation()
    # Set slide dimensions to 16:9 widescreen (13.333 x 7.5 inches)
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    
    # Blank slide layout
    blank_layout = prs.slide_layouts[6]
    
    # Color palette
    BG_DARK = RGBColor(15, 23, 42)        # #0f172a (Deep Slate)
    CARD_BG = RGBColor(30, 41, 59)        # #1e293b (Slate Gray)
    CARD_BORDER = RGBColor(51, 65, 85)    # #334155 (Border Slate)
    TEXT_MAIN = RGBColor(248, 250, 252)   # #f8fafc (Pure Light)
    TEXT_MUTED = RGBColor(148, 163, 184) # #94a3b8 (Soft Gray)
    ACCENT_CYAN = RGBColor(6, 182, 212)   # #06b6d4 (Cyan AI)
    ACCENT_EMERALD = RGBColor(16, 185, 129)# #10b981 (Finance Emerald)
    ACCENT_PURPLE = RGBColor(168, 85, 247) # #a855f7 (Purple Accent)
    ACCENT_AMBER = RGBColor(245, 158, 11) # #f59e0b (Amber Accent)

    def set_bg(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = BG_DARK
        bg.line.fill.background()
        return bg

    def add_header(slide, title_text, category_tag="SMARTEXPENSE AI"):
        # Header Container
        header_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(11.733), Inches(1.2))
        tf = header_box.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        
        # Tag
        p_tag = tf.paragraphs[0]
        p_tag.text = category_tag.upper()
        p_tag.font.size = Pt(11)
        p_tag.font.bold = True
        p_tag.font.color.rgb = ACCENT_CYAN
        p_tag.space_after = Pt(4)
        
        # Main Title
        p_title = tf.add_paragraph()
        p_title.text = title_text
        p_title.font.size = Pt(28)
        p_title.font.bold = True
        p_title.font.color.rgb = TEXT_MAIN

    def add_card(slide, left, top, width, height, bg_color=CARD_BG, border_color=CARD_BORDER):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        card.line.color.rgb = border_color
        card.line.width = Pt(1)
        return card

    # ==========================================
    # SLIDE 1: TITLE PAGE
    # ==========================================
    slide1 = prs.slides.add_slide(blank_layout)
    set_bg(slide1)

    # Decorative background glow effect (card behind)
    add_card(slide1, Inches(0.8), Inches(0.8), Inches(11.733), Inches(5.9), bg_color=CARD_BG, border_color=ACCENT_CYAN)

    # Title content frame
    t_box = slide1.shapes.add_textbox(Inches(1.2), Inches(1.2), Inches(10.933), Inches(2.2))
    tf1 = t_box.text_frame
    tf1.word_wrap = True

    p_badge = tf1.paragraphs[0]
    p_badge.text = "PROPOSED TINY AI PROTOTYPE CONCEPT"
    p_badge.font.size = Pt(12)
    p_badge.font.bold = True
    p_badge.font.color.rgb = ACCENT_CYAN
    p_badge.space_after = Pt(10)

    p_main = tf1.add_paragraph()
    p_main.text = "SmartExpense AI"
    p_main.font.size = Pt(44)
    p_main.font.bold = True
    p_main.font.color.rgb = TEXT_MAIN
    p_main.space_after = Pt(8)

    p_sub = tf1.add_paragraph()
    p_sub.text = "An Intelligent AI-Based Expense Classification System"
    p_sub.font.size = Pt(22)
    p_sub.font.color.rgb = ACCENT_EMERALD
    p_sub.space_after = Pt(6)

    p_tagline = tf1.add_paragraph()
    p_tagline.text = "Tiny AI Project Presentation"
    p_tagline.font.size = Pt(16)
    p_tagline.font.color.rgb = TEXT_MUTED

    # Team Box inside slide 1
    team_card = add_card(slide1, Inches(1.2), Inches(3.7), Inches(10.933), Inches(2.5), bg_color=RGBColor(24, 34, 53), border_color=CARD_BORDER)
    team_tf = team_card.text_frame
    team_tf.word_wrap = True
    team_tf.margin_left = Inches(0.4)
    team_tf.margin_top = Inches(0.3)

    p_t_head = team_tf.paragraphs[0]
    p_t_head.text = "PROJECT TEAM MEMBERS"
    p_t_head.font.size = Pt(13)
    p_t_head.font.bold = True
    p_t_head.font.color.rgb = ACCENT_CYAN
    p_t_head.space_after = Pt(12)

    members = [
        ("1. Mayank Mali", "Roll No. 85"),
        ("2. Priyanshi Pitroda", "Roll No. 106"),
        ("3. Deepak Kansara", "Roll No. 53")
    ]

    # Create 3 columns for team members
    for idx, (name, roll) in enumerate(members):
        col_box = slide1.shapes.add_textbox(Inches(1.5 + idx * 3.5), Inches(4.3), Inches(3.2), Inches(1.5))
        ctf = col_box.text_frame
        ctf.word_wrap = True
        
        p1 = ctf.paragraphs[0]
        p1.text = name
        p1.font.size = Pt(18)
        p1.font.bold = True
        p1.font.color.rgb = TEXT_MAIN
        
        p2 = ctf.add_paragraph()
        p2.text = roll
        p2.font.size = Pt(14)
        p2.font.color.rgb = ACCENT_EMERALD

    # ==========================================
    # SLIDE 2: INTRODUCTION
    # ==========================================
    slide2 = prs.slides.add_slide(blank_layout)
    set_bg(slide2)
    add_header(slide2, "Introduction to SmartExpense AI")

    # Left Column: System Overview Card
    add_card(slide2, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0))
    tb_left = slide2.shapes.add_textbox(Inches(1.1), Inches(2.1), Inches(5.0), Inches(4.4))
    tf2_l = tb_left.text_frame
    tf2_l.word_wrap = True

    p = tf2_l.paragraphs[0]
    p.text = "What is SmartExpense AI?"
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = ACCENT_CYAN
    p.space_after = Pt(14)

    bullets_l = [
        "SmartExpense AI is an intelligent lightweight AI-based system.",
        "It automatically categorizes user expenses based on plain-text expense descriptions.",
        "Eliminates manual category selection during daily expense logging.",
        "Leverages Tiny AI principles to ensure fast, efficient, and resource-friendly classification."
    ]
    for b in bullets_l:
        pb = tf2_l.add_paragraph()
        pb.text = "• " + b
        pb.font.size = Pt(15)
        pb.font.color.rgb = TEXT_MAIN
        pb.space_after = Pt(10)

    # Right Column: Visual Examples Card
    add_card(slide2, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.0))
    tb_right = slide2.shapes.add_textbox(Inches(7.1), Inches(2.1), Inches(5.1), Inches(4.4))
    tf2_r = tb_right.text_frame
    tf2_r.word_wrap = True

    p_ex_title = tf2_r.paragraphs[0]
    p_ex_title.text = "Automated Categorization Examples"
    p_ex_title.font.size = Pt(20)
    p_ex_title.font.bold = True
    p_ex_title.font.color.rgb = ACCENT_EMERALD
    p_ex_title.space_after = Pt(16)

    examples = [
        ("₹250 – Pizza", "Food", "🍔"),
        ("₹800 – Uber", "Travel", "🚗"),
        ("₹1,500 – Shoes", "Shopping", "🛍️")
    ]

    for input_txt, cat, icon in examples:
        # Create small mini card inside right col
        p_in = tf2_r.add_paragraph()
        p_in.text = f"Input: \"{input_txt}\""
        p_in.font.size = Pt(15)
        p_in.font.bold = True
        p_in.font.color.rgb = TEXT_MUTED

        p_out = tf2_r.add_paragraph()
        p_out.text = f"➜ AI Prediction: {icon} {cat}"
        p_out.font.size = Pt(17)
        p_out.font.bold = True
        p_out.font.color.rgb = ACCENT_CYAN
        p_out.space_after = Pt(12)

    # Bottom summary box in right col
    p_sum = tf2_r.add_paragraph()
    p_sum.text = "AI transforms raw transaction text into structured financial data instantly, saving time and increasing accuracy."
    p_sum.font.size = Pt(14)
    p_sum.font.italic = True
    p_sum.font.color.rgb = TEXT_MUTED

    # ==========================================
    # SLIDE 3: PROBLEM STATEMENT
    # ==========================================
    slide3 = prs.slides.add_slide(blank_layout)
    set_bg(slide3)
    add_header(slide3, "Problem Statement: Challenges in Manual Expense Tracking")

    problems = [
        ("Manual Categorization Effort", "Users have to manually select tags and categories for every single purchase daily, leading to friction.", "⏳"),
        ("Time-Consuming Process", "Logging transactions individually consumes unnecessary time and leads to tracking fatigue.", "⏱️"),
        ("Small Expenses Ignored", "Minor daily expenses (coffee, snacks, auto fare) are frequently skipped, resulting in inaccurate budgets.", "💸"),
        ("Unclear Spending Patterns", "Unorganized raw transaction data makes it difficult to analyze monthly cash flow effectively.", "📊"),
        ("Inconsistent Category Tags", "Different tags used for similar items over time create confusing and scattered reports.", "⚠️")
    ]

    # Grid of 5 cards (2 rows: row1=3 cards, row2=2 cards)
    for i, (p_title, p_desc, icon) in enumerate(problems):
        if i < 3:
            left = Inches(0.8 + i * 3.96)
            top = Inches(1.8)
            width = Inches(3.8)
            height = Inches(2.4)
        else:
            left = Inches(2.78 + (i - 3) * 3.96)
            top = Inches(4.4)
            width = Inches(3.8)
            height = Inches(2.4)

        add_card(slide3, left, top, width, height)
        tb = slide3.shapes.add_textbox(left + Inches(0.2), top + Inches(0.2), width - Inches(0.4), height - Inches(0.4))
        tf = tb.text_frame
        tf.word_wrap = True

        p1 = tf.paragraphs[0]
        p1.text = f"{icon}  {p_title}"
        p1.font.size = Pt(16)
        p1.font.bold = True
        p1.font.color.rgb = ACCENT_AMBER
        p1.space_after = Pt(8)

        p2 = tf.add_paragraph()
        p2.text = p_desc
        p2.font.size = Pt(13)
        p2.font.color.rgb = TEXT_MUTED

    # ==========================================
    # SLIDE 4: OBJECTIVES
    # ==========================================
    slide4 = prs.slides.add_slide(blank_layout)
    set_bg(slide4)
    add_header(slide4, "Project Objectives")

    objectives = [
        ("Automate Expense Classification", "Automatically identify and tag transaction categories directly from text descriptions.", ACCENT_CYAN),
        ("Minimize User Effort", "Significantly reduce manual data entry and tagging effort for everyday financial logs.", ACCENT_EMERALD),
        ("Organize Financial Data", "Structure raw transaction logs into clean, categorized financial buckets for quick viewing.", ACCENT_PURPLE),
        ("Demonstrate Tiny AI Concept", "Showcase how a compact ML model performs accurate classification with low computation.", ACCENT_AMBER),
        ("Simple & Accessible UI", "Provide a minimal, intuitive interface suitable for students and everyday users.", ACCENT_CYAN),
        ("Financial Awareness", "Help users effortlessly track spending habits and improve overall budgeting.", ACCENT_EMERALD)
    ]

    for idx, (title, desc, accent) in enumerate(objectives):
        col = idx % 3
        row = idx // 3
        left = Inches(0.8 + col * 3.96)
        top = Inches(1.8 + row * 2.6)
        width = Inches(3.8)
        height = Inches(2.4)

        card = add_card(slide4, left, top, width, height)
        tb = slide4.shapes.add_textbox(left + Inches(0.25), top + Inches(0.25), width - Inches(0.5), height - Inches(0.5))
        tf = tb.text_frame
        tf.word_wrap = True

        p1 = tf.paragraphs[0]
        p1.text = f"0{idx+1}. {title}"
        p1.font.size = Pt(16)
        p1.font.bold = True
        p1.font.color.rgb = accent
        p1.space_after = Pt(8)

        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(13)
        p2.font.color.rgb = TEXT_MAIN

    # ==========================================
    # SLIDE 5: PROPOSED SOLUTION
    # ==========================================
    slide5 = prs.slides.add_slide(blank_layout)
    set_bg(slide5)
    add_header(slide5, "Proposed Solution: Intelligent Workflow")

    # Workflow Steps horizontal sequence
    steps = [
        ("User Enters Expense", "Plain text entry", "📝"),
        ("Expense Description", "\"₹300 - Dinner...\"", "💬"),
        ("Text Preprocessing", "Clean & tokenize", "⚙️"),
        ("Tiny AI Model", "Classify intent", "🤖"),
        ("Predicted Category", "Assign 'Food'", "🏷️"),
        ("Expense Dashboard", "Update analytics", "📊")
    ]

    for idx, (step_title, sub, icon) in enumerate(steps):
        left = Inches(0.8 + idx * 1.98)
        top = Inches(2.0)
        width = Inches(1.8)
        height = Inches(2.5)

        card = add_card(slide5, left, top, width, height, bg_color=CARD_BG, border_color=ACCENT_CYAN)
        tb = slide5.shapes.add_textbox(left + Inches(0.1), top + Inches(0.15), width - Inches(0.2), height - Inches(0.3))
        tf = tb.text_frame
        tf.word_wrap = True

        p0 = tf.paragraphs[0]
        p0.text = icon
        p0.font.size = Pt(24)
        p0.alignment = PP_ALIGN.CENTER
        p0.space_after = Pt(6)

        p1 = tf.add_paragraph()
        p1.text = f"Step {idx+1}"
        p1.font.size = Pt(11)
        p1.font.bold = True
        p1.font.color.rgb = ACCENT_CYAN
        p1.alignment = PP_ALIGN.CENTER

        p2 = tf.add_paragraph()
        p2.text = step_title
        p2.font.size = Pt(13)
        p2.font.bold = True
        p2.font.color.rgb = TEXT_MAIN
        p2.alignment = PP_ALIGN.CENTER
        p2.space_after = Pt(4)

        p3 = tf.add_paragraph()
        p3.text = sub
        p3.font.size = Pt(11)
        p3.font.color.rgb = TEXT_MUTED
        p3.alignment = PP_ALIGN.CENTER

    # Example Card Below Workflow
    add_card(slide5, Inches(0.8), Inches(4.8), Inches(11.733), Inches(2.0), bg_color=RGBColor(20, 30, 48), border_color=ACCENT_EMERALD)
    tb_ex = slide5.shapes.add_textbox(Inches(1.1), Inches(5.0), Inches(11.133), Inches(1.6))
    tf_ex = tb_ex.text_frame
    tf_ex.word_wrap = True

    pe1 = tf_ex.paragraphs[0]
    pe1.text = "PROPOSED WORKFLOW EXAMPLE IN ACTION"
    pe1.font.size = Pt(13)
    pe1.font.bold = True
    pe1.font.color.rgb = ACCENT_EMERALD
    pe1.space_after = Pt(8)

    pe2 = tf_ex.add_paragraph()
    pe2.text = "Input Description:  \"₹300 – Dinner at restaurant\""
    pe2.font.size = Pt(18)
    pe2.font.bold = True
    pe2.font.color.rgb = TEXT_MAIN

    pe3 = tf_ex.add_paragraph()
    pe3.text = "➜ Tiny AI Prediction:  Food (Category auto-assigned to budget tracker)"
    pe3.font.size = Pt(18)
    pe3.font.bold = True
    pe3.font.color.rgb = ACCENT_CYAN

    # ==========================================
    # SLIDE 6: HOW THE AI WORKS
    # ==========================================
    slide6 = prs.slides.add_slide(blank_layout)
    set_bg(slide6)
    add_header(slide6, "How the Tiny AI Engine Works")

    ai_steps = [
        ("1. Input Reception", "System captures raw expense text provided by the user."),
        ("2. Text Cleaning", "Removes special symbols, converts to lowercase, & normalizes words."),
        ("3. Feature Extraction", "Converts processed text into numerical feature vectors."),
        ("4. Tiny AI Inference", "Lightweight ML classification model analyzes feature weights."),
        ("5. Category Prediction", "Model outputs the category with highest probability match."),
        ("6. Dashboard Display", "Category is automatically rendered on user's finance dashboard.")
    ]

    for idx, (title, desc) in enumerate(ai_steps):
        col = idx % 2
        row = idx // 2
        left = Inches(0.8 + col * 5.96)
        top = Inches(1.8 + row * 1.5)
        width = Inches(5.7)
        height = Inches(1.3)

        add_card(slide6, left, top, width, height)
        tb = slide6.shapes.add_textbox(left + Inches(0.2), top + Inches(0.15), width - Inches(0.4), height - Inches(0.3))
        tf = tb.text_frame
        tf.word_wrap = True

        p1 = tf.paragraphs[0]
        p1.text = title
        p1.font.size = Pt(16)
        p1.font.bold = True
        p1.font.color.rgb = ACCENT_CYAN
        p1.space_after = Pt(4)

        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(13)
        p2.font.color.rgb = TEXT_MAIN

    # Highlight Card at bottom
    add_card(slide6, Inches(0.8), Inches(6.0), Inches(11.733), Inches(0.9), bg_color=RGBColor(30, 27, 75), border_color=ACCENT_PURPLE)
    tb_hl = slide6.shapes.add_textbox(Inches(1.0), Inches(6.1), Inches(11.333), Inches(0.7))
    tf_hl = tb_hl.text_frame
    tf_hl.word_wrap = True

    ph = tf_hl.paragraphs[0]
    ph.text = "💡 Tiny AI Advantage: Lightweight classification model allows instant predictions with low computational overhead, perfect for edge devices and lightweight web prototypes."
    ph.font.size = Pt(14)
    ph.font.bold = True
    ph.font.color.rgb = RGBColor(224, 231, 255)

    # ==========================================
    # SLIDE 7: EXPENSE CATEGORIES
    # ==========================================
    slide7 = prs.slides.add_slide(blank_layout)
    set_bg(slide7)
    add_header(slide7, "Supported Expense Categories")

    categories = [
        ("Food & Dining", "🍔", "Restaurants, groceries, snacks, coffee, food delivery", ACCENT_EMERALD),
        ("Travel & Transit", "🚗", "Uber, cabs, fuel, train, flight, parking tickets", ACCENT_CYAN),
        ("Shopping", "🛍️", "Clothing, electronics, online store orders", ACCENT_PURPLE),
        ("Education", "📚", "Books, online courses, college tuition, stationary", ACCENT_AMBER),
        ("Entertainment", "🎬", "Movies, streaming services, concerts, gaming", RGBColor(244, 63, 94)),
        ("Bills & Utilities", "💡", "Electricity, internet, water bills, recharge", RGBColor(14, 165, 233)),
        ("Others / Misc", "📦", "Unspecified or general daily miscellaneous items", TEXT_MUTED)
    ]

    # Grid of visual cards
    for idx, (c_name, icon, c_desc, color) in enumerate(categories):
        if idx < 4:
            left = Inches(0.8 + idx * 2.96)
            top = Inches(1.8)
            width = Inches(2.8)
            height = Inches(2.4)
        else:
            left = Inches(1.5 + (idx - 4) * 3.5)
            top = Inches(4.5)
            width = Inches(3.3)
            height = Inches(2.3)

        add_card(slide7, left, top, width, height, bg_color=CARD_BG, border_color=color)
        tb = slide7.shapes.add_textbox(left + Inches(0.15), top + Inches(0.15), width - Inches(0.3), height - Inches(0.3))
        tf = tb.text_frame
        tf.word_wrap = True

        p0 = tf.paragraphs[0]
        p0.text = icon
        p0.font.size = Pt(28)
        p0.space_after = Pt(4)

        p1 = tf.add_paragraph()
        p1.text = c_name
        p1.font.size = Pt(16)
        p1.font.bold = True
        p1.font.color.rgb = color
        p1.space_after = Pt(6)

        p2 = tf.add_paragraph()
        p2.text = c_desc
        p2.font.size = Pt(12)
        p2.font.color.rgb = TEXT_MUTED

    # ==========================================
    # SLIDE 8: SYSTEM ARCHITECTURE
    # ==========================================
    slide8 = prs.slides.add_slide(blank_layout)
    set_bg(slide8)
    add_header(slide8, "System Architecture Diagram")

    # Clean flow architecture
    arch_nodes = [
        ("User", "Client Interaction", "👤"),
        ("Expense Input", "Raw Description Text", "💬"),
        ("Preprocessing", "Tokenize & Clean Text", "⚙️"),
        ("Feature Extraction", "Vector Feature Matrix", "🔍"),
        ("Tiny AI Model", "Classifier Inference", "🤖"),
        ("Category Prediction", "Assigned Label", "🏷️"),
        ("Expense Dashboard", "UI Analytics Display", "📊")
    ]

    for idx, (title, detail, icon) in enumerate(arch_nodes):
        left = Inches(0.8 + idx * 1.69)
        top = Inches(2.6)
        width = Inches(1.55)
        height = Inches(3.0)

        card = add_card(slide8, left, top, width, height, bg_color=CARD_BG, border_color=ACCENT_CYAN)
        tb = slide8.shapes.add_textbox(left + Inches(0.08), top + Inches(0.2), width - Inches(0.16), height - Inches(0.4))
        tf = tb.text_frame
        tf.word_wrap = True

        p0 = tf.paragraphs[0]
        p0.text = f"Layer {idx+1}"
        p0.font.size = Pt(10)
        p0.font.bold = True
        p0.font.color.rgb = ACCENT_EMERALD
        p0.alignment = PP_ALIGN.CENTER
        p0.space_after = Pt(8)

        p1 = tf.add_paragraph()
        p1.text = icon
        p1.font.size = Pt(26)
        p1.alignment = PP_ALIGN.CENTER
        p1.space_after = Pt(8)

        p2 = tf.add_paragraph()
        p2.text = title
        p2.font.size = Pt(13)
        p2.font.bold = True
        p2.font.color.rgb = TEXT_MAIN
        p2.alignment = PP_ALIGN.CENTER
        p2.space_after = Pt(6)

        p3 = tf.add_paragraph()
        p3.text = detail
        p3.font.size = Pt(10)
        p3.font.color.rgb = TEXT_MUTED
        p3.alignment = PP_ALIGN.CENTER

    # Note at bottom
    add_card(slide8, Inches(0.8), Inches(6.0), Inches(11.733), Inches(0.9), bg_color=RGBColor(15, 30, 45), border_color=ACCENT_CYAN)
    tb_an = slide8.shapes.add_textbox(Inches(1.0), Inches(6.1), Inches(11.333), Inches(0.7))
    tf_an = tb_an.text_frame
    tf_an.word_wrap = True
    pa = tf_an.paragraphs[0]
    pa.text = "Modular Architecture: Simple pipeline allowing real-time text processing from User Input to Dashboard visual rendering."
    pa.font.size = Pt(13)
    pa.font.color.rgb = TEXT_MAIN

    # ==========================================
    # SLIDE 9: TECHNOLOGY STACK
    # ==========================================
    slide9 = prs.slides.add_slide(blank_layout)
    set_bg(slide9)
    add_header(slide9, "Proposed Technology Stack")

    stacks = [
        ("Frontend", "HTML5, CSS3, JavaScript", "Provides a modern, responsive user interface for entering expenses and displaying live category results.", "🖥️", ACCENT_CYAN),
        ("Backend", "Python / Flask", "Lightweight REST API framework to handle client requests and feed data to the AI model.", "🐍", ACCENT_EMERALD),
        ("AI / ML Model", "Lightweight ML Classifier (Python)", "Compact Scikit-Learn based classification model optimized for low memory usage.", "🤖", ACCENT_PURPLE),
        ("Data Storage", "CSV / SQLite", "Simple structured storage solution for persisting categorized expense records and user history.", "🗄️", ACCENT_AMBER)
    ]

    for idx, (tech_type, tech_stack, desc, icon, color) in enumerate(stacks):
        left = Inches(0.8 + idx * 2.96)
        top = Inches(1.8)
        width = Inches(2.8)
        height = Inches(4.3)

        add_card(slide9, left, top, width, height, bg_color=CARD_BG, border_color=color)
        tb = slide9.shapes.add_textbox(left + Inches(0.2), top + Inches(0.2), width - Inches(0.4), height - Inches(0.4))
        tf = tb.text_frame
        tf.word_wrap = True

        p0 = tf.paragraphs[0]
        p0.text = icon
        p0.font.size = Pt(32)
        p0.space_after = Pt(8)

        p1 = tf.add_paragraph()
        p1.text = tech_type
        p1.font.size = Pt(18)
        p1.font.bold = True
        p1.font.color.rgb = color
        p1.space_after = Pt(6)

        p2 = tf.add_paragraph()
        p2.text = tech_stack
        p2.font.size = Pt(14)
        p2.font.bold = True
        p2.font.color.rgb = TEXT_MAIN
        p2.space_after = Pt(10)

        p3 = tf.add_paragraph()
        p3.text = desc
        p3.font.size = Pt(12)
        p3.font.color.rgb = TEXT_MUTED

    # Mandatory Disclaimer Banner
    add_card(slide9, Inches(0.8), Inches(6.3), Inches(11.733), Inches(0.7), bg_color=RGBColor(45, 20, 20), border_color=RGBColor(239, 68, 68))
    tb_disc = slide9.shapes.add_textbox(Inches(1.0), Inches(6.35), Inches(11.333), Inches(0.6))
    tf_disc = tb_disc.text_frame
    tf_disc.word_wrap = True
    pd = tf_disc.paragraphs[0]
    pd.text = "📌 Note: These are proposed technologies for the prototype concept presentation."
    pd.font.size = Pt(13)
    pd.font.bold = True
    pd.font.color.rgb = RGBColor(254, 202, 202)

    # ==========================================
    # SLIDE 10: SAMPLE INPUT & OUTPUT
    # ==========================================
    slide10 = prs.slides.add_slide(blank_layout)
    set_bg(slide10)
    add_header(slide10, "Sample Input & Output Mapping")

    # Table creation
    rows = 6
    cols = 3
    table_shape = slide10.shapes.add_table(rows, cols, Inches(0.8), Inches(1.8), Inches(11.733), Inches(4.3))
    table = table_shape.table

    table.columns[0].width = Inches(1.5)
    table.columns[1].width = Inches(6.233)
    table.columns[2].width = Inches(4.0)

    table_data = [
        ("Sample #", "Input Expense Description", "AI Predicted Category"),
        ("01", "\"₹250 – Pizza\"", "🍔  Food"),
        ("02", "\"₹500 – Uber Ride\"", "🚗  Travel"),
        ("03", "\"₹1,200 – T-Shirt\"", "🛍️  Shopping"),
        ("04", "\"₹900 – Movie Ticket\"", "🎬  Entertainment"),
        ("05", "\"₹2,000 – Course Fee\"", "📚  Education")
    ]

    for r_idx, row in enumerate(table_data):
        for c_idx, val in enumerate(row):
            cell = table.cell(r_idx, c_idx)
            cell.text = val
            cell.fill.solid()
            if r_idx == 0:
                cell.fill.fore_color.rgb = RGBColor(30, 58, 138)
            else:
                cell.fill.fore_color.rgb = CARD_BG if r_idx % 2 == 1 else RGBColor(24, 34, 53)
            
            p = cell.text_frame.paragraphs[0]
            p.font.size = Pt(14)
            p.font.bold = (r_idx == 0 or c_idx == 2)
            p.font.color.rgb = ACCENT_CYAN if (r_idx == 0 or c_idx == 2) else TEXT_MAIN

    # Explanatory card below table
    add_card(slide10, Inches(0.8), Inches(6.3), Inches(11.733), Inches(0.7))
    tb_t_desc = slide10.shapes.add_textbox(Inches(1.0), Inches(6.35), Inches(11.333), Inches(0.6))
    tf_td = tb_t_desc.text_frame
    tf_td.word_wrap = True
    ptd = tf_td.paragraphs[0]
    ptd.text = "Explanation: The AI classification model analyzes the text context and keywords to infer the accurate expense category."
    ptd.font.size = Pt(13)
    ptd.font.color.rgb = TEXT_MUTED

    # ==========================================
    # SLIDE 11: ADVANTAGES & APPLICATIONS
    # ==========================================
    slide11 = prs.slides.add_slide(blank_layout)
    set_bg(slide11)
    add_header(slide11, "Advantages & Potential Applications")

    # Left: Advantages
    add_card(slide11, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.1))
    tb_adv = slide11.shapes.add_textbox(Inches(1.1), Inches(2.0), Inches(5.0), Inches(4.7))
    tf_adv = tb_adv.text_frame
    tf_adv.word_wrap = True

    pa_head = tf_adv.paragraphs[0]
    pa_head.text = "Key System Advantages"
    pa_head.font.size = Pt(20)
    pa_head.font.bold = True
    pa_head.font.color.rgb = ACCENT_EMERALD
    pa_head.space_after = Pt(12)

    advs = [
        "Saves Time: Eliminates tedious manual category selection.",
        "Reduces Manual Categorization: Automated text parsing handles classification.",
        "Simple & Intuitive to Use: Zero learning curve for end users.",
        "Lightweight AI Approach: Efficient execution suited for Tiny AI concepts.",
        "Easy Integration: Seamlessly embeddable into existing expense apps."
    ]
    for a in advs:
        p = tf_adv.add_paragraph()
        p.text = "✔ " + a
        p.font.size = Pt(14)
        p.font.color.rgb = TEXT_MAIN
        p.space_after = Pt(10)

    # Right: Applications
    add_card(slide11, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.1))
    tb_app = slide11.shapes.add_textbox(Inches(7.1), Inches(2.0), Inches(5.1), Inches(4.7))
    tf_app = tb_app.text_frame
    tf_app.word_wrap = True

    papp_head = tf_app.paragraphs[0]
    papp_head.text = "Practical Applications"
    papp_head.font.size = Pt(20)
    papp_head.font.bold = True
    papp_head.font.color.rgb = ACCENT_CYAN
    papp_head.space_after = Pt(12)

    apps = [
        "Personal Finance Apps: Enhance daily logging experience.",
        "Student Expense Tracking: Simple budgeting tool for college students.",
        "Small Business Expense Mgmt: Fast categorization for micro receipts.",
        "Budgeting Applications: Auto-group monthly spend into buckets.",
        "Mobile Finance Assistants: On-device lightweight smart assistant."
    ]
    for ap in apps:
        p = tf_app.add_paragraph()
        p.text = "🚀 " + ap
        p.font.size = Pt(14)
        p.font.color.rgb = TEXT_MAIN
        p.space_after = Pt(10)

    # ==========================================
    # SLIDE 12: FUTURE SCOPE & CONCLUSION
    # ==========================================
    slide12 = prs.slides.add_slide(blank_layout)
    set_bg(slide12)
    add_header(slide12, "Future Scope & Conclusion")

    # Left: Future Scope
    add_card(slide12, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.1))
    tb_fut = slide12.shapes.add_textbox(Inches(1.1), Inches(2.0), Inches(5.0), Inches(4.7))
    tf_fut = tb_fut.text_frame
    tf_fut.word_wrap = True

    pf_head = tf_fut.paragraphs[0]
    pf_head.text = "Future Scope & Enhancements"
    pf_head.font.size = Pt(20)
    pf_head.font.bold = True
    pf_head.font.color.rgb = ACCENT_PURPLE
    pf_head.space_after = Pt(12)

    futs = [
        "Automatic monthly spending analysis & visualization",
        "Smart AI budget recommendations & alerts",
        "Anomalous spending trend detection",
        "Voice-based expense entry integration",
        "Dedicated mobile application build",
        "Personalized financial health insights"
    ]
    for f in futs:
        p = tf_fut.add_paragraph()
        p.text = "🔮 " + f
        p.font.size = Pt(14)
        p.font.color.rgb = TEXT_MAIN
        p.space_after = Pt(8)

    # Right: Conclusion Card
    add_card(slide12, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.1), bg_color=RGBColor(24, 34, 53), border_color=ACCENT_EMERALD)
    tb_conc = slide12.shapes.add_textbox(Inches(7.1), Inches(2.2), Inches(5.1), Inches(4.3))
    tf_conc = tb_conc.text_frame
    tf_conc.word_wrap = True

    pc_head = tf_conc.paragraphs[0]
    pc_head.text = "Conclusion"
    pc_head.font.size = Pt(22)
    pc_head.font.bold = True
    pc_head.font.color.rgb = ACCENT_EMERALD
    pc_head.space_after = Pt(16)

    pc_quote = tf_conc.add_paragraph()
    pc_quote.text = "“SmartExpense AI demonstrates how a lightweight AI model can automate expense classification and make financial tracking simpler and more organized.”"
    pc_quote.font.size = Pt(18)
    pc_quote.font.bold = True
    pc_quote.font.color.rgb = TEXT_MAIN
    pc_quote.space_after = Pt(16)

    pc_sub = tf_conc.add_paragraph()
    pc_sub.text = "This proposed prototype highlights the power of Tiny AI in streamlining everyday utility tasks without demanding high computing power."
    pc_sub.font.size = Pt(14)
    pc_sub.font.color.rgb = TEXT_MUTED

    # ==========================================
    # SLIDE 13: THANK YOU
    # ==========================================
    slide13 = prs.slides.add_slide(blank_layout)
    set_bg(slide13)

    add_card(slide13, Inches(1.5), Inches(1.2), Inches(10.333), Inches(5.1), bg_color=CARD_BG, border_color=ACCENT_CYAN)

    tb_ty = slide13.shapes.add_textbox(Inches(1.8), Inches(2.0), Inches(9.733), Inches(3.5))
    tf_ty = tb_ty.text_frame
    tf_ty.word_wrap = True

    pty1 = tf_ty.paragraphs[0]
    pty1.text = "THANK YOU"
    pty1.font.size = Pt(48)
    pty1.font.bold = True
    pty1.font.color.rgb = ACCENT_CYAN
    pty1.alignment = PP_ALIGN.CENTER
    pty1.space_after = Pt(12)

    pty2 = tf_ty.add_paragraph()
    pty2.text = "Questions & Discussion"
    pty2.font.size = Pt(24)
    pty2.font.color.rgb = ACCENT_EMERALD
    pty2.alignment = PP_ALIGN.CENTER
    pty2.space_after = Pt(24)

    pty3 = tf_ty.add_paragraph()
    pty3.text = "SmartExpense AI – Tiny AI Project Presentation"
    pty3.font.size = Pt(16)
    pty3.font.color.rgb = TEXT_MUTED
    pty3.alignment = PP_ALIGN.CENTER

    output_path = r"C:\Users\malim\.gemini\antigravity-ide\scratch\SmartExpense_AI_Presentation\SmartExpense_AI_Presentation.pptx"
    prs.save(output_path)
    print(f"Presentation saved successfully at {output_path}")

if __name__ == "__main__":
    create_presentation()
