from crewai import Crew, Task, Process, LLM
from agents import linkedin_writer, twitter_writer, instagram_writer, facebook_writer, create_post_humanizer, create_post_reviewer
from tasks import generate_linkedin_post, generate_twitter_post, generate_instagram_post, generate_facebook_post, humanize_post, review_final_post
from dotenv import load_dotenv

# load_dotenv()

def create_crew(platform, industry, company_info, product_info, llm):
    if platform == "LinkedIn":
        writer = linkedin_writer(llm = llm)
        task = generate_linkedin_post
    elif platform == "Twitter":
        writer = twitter_writer(llm=llm)
        task = generate_twitter_post
    elif platform == "Instagram":
        writer = instagram_writer(llm=llm)  
        task = generate_instagram_post
    elif platform == "Facebook":
        writer = facebook_writer(llm=llm)
        task = generate_facebook_post
    else:
        raise ValueError("Unsupported platform!")

    # Formatting task descriptions with user inputs
    writer_task = Task(description=task["description"].format(
        industry=industry, company_info=company_info, product_info=product_info),
        expected_output=task["expected_output"],
        agent=writer
    )
    post_humanizer = create_post_humanizer(llm)
    post_reviewer = create_post_reviewer(llm)

    humanizer_task = Task(description=humanize_post["description"],
                          expected_output=humanize_post["expected_output"],
                          agent=post_humanizer)

    review_task = Task(description=review_final_post["description"],
                       expected_output=review_final_post["expected_output"],
                       agent=post_reviewer)

    # Crew formation
    crew = Crew(
        agents=[writer, post_humanizer, post_reviewer],
        tasks=[writer_task, humanizer_task, review_task],
        process=Process.sequential
    )

    return crew
