from crewai import Agent
def linkedin_writer(llm):
    return Agent(
        role="LinkedIn Content Specialist",
        goal="Craft professional and insightful LinkedIn posts for industry professionals.",
        backstory="Expert in LinkedIn content writing, specializing in structured and thought-leadership posts.",
        verbose=True,
        memory=True,
        llm=llm
    )

def twitter_writer(llm):
    return Agent(
        role="Twitter Content Strategist",
        goal="Create engaging, concise, and shareable Twitter posts.",
        backstory="Expert in crafting short, witty, and viral tweets that drive engagement.",
        verbose=True,
        memory=True,
        llm=llm
    )

def instagram_writer(llm):
    return Agent(
        role="Instagram Caption Specialist",
        goal="Write catchy and trendy Instagram captions.",
        backstory="Creative writer who specializes in fun, engaging, and eye-catching captions.",
        verbose=True,
        memory=True,
        llm=llm
    )

def facebook_writer(llm):
    return Agent(
        role="Facebook Community Manager",
        goal="Write engaging, story-driven, and conversational Facebook posts.",
        backstory="Expert in long-form, engaging, and interactive Facebook posts.",
        verbose=True,
        memory=True,
        llm=llm
    )

def create_post_humanizer(llm):
    return Agent(
        role="Social Media Content Humanizer",
        goal="Refine and enhance posts to make them sound natural and engaging.",
        backstory="Ensures content flows naturally, is emotionally engaging, and feels human-written.",
        verbose=True,
        memory=True,
        llm=llm
    )

def create_post_reviewer(llm):
    return Agent(
        role="Social Media Content Reviewer",
        goal="Conduct a final review to ensure clarity, impact, and engagement before publishing.",
        backstory="Expert in social media trends, ensuring platform optimization and readability.",
        verbose=True,
        memory=True,
        llm=llm
    )
# linkedin_writer = Agent(
#     role="LinkedIn Content Specialist",
#     goal="Craft professional and insightful LinkedIn posts for industry professionals.",
#     backstory="Expert in LinkedIn content writing, specializing in structured and thought-leadership posts.",
#     verbose=True,
#     memory=True
# )

# twitter_writer = Agent(
#     role="Twitter Content Strategist",
#     goal="Create engaging, concise, and shareable Twitter posts.",
#     backstory="Expert in crafting short, witty, and viral tweets that drive engagement.",
#     verbose=True,
#     memory=True
# )

# instagram_writer = Agent(
#     role="Instagram Caption Specialist",
#     goal="Write catchy and trendy Instagram captions.",
#     backstory="Creative writer who specializes in fun, engaging, and eye-catching captions.",
#     verbose=True,
#     memory=True
# )

# facebook_writer = Agent(
#     role="Facebook Community Manager",
#     goal="Write engaging, story-driven, and conversational Facebook posts.",
#     backstory="Expert in long-form, engaging, and interactive Facebook posts.",
#     verbose=True,
#     memory=True
# )

# post_humanizer = Agent(
#     role="Social Media Content Humanizer",
#     goal="Refine and enhance posts to make them sound natural and engaging.",
#     backstory="Ensures content flows naturally, is emotionally engaging, and feels human-written.",
#     verbose=True,
#     memory=True
# )

# post_reviewer = Agent(
#     role="Social Media Content Reviewer",
#     goal="Conduct a final review to ensure clarity, impact, and engagement before publishing.",
#     backstory="Expert in social media trends, ensuring platform optimization and readability.",
#     verbose=True,
#     memory=True
# )
