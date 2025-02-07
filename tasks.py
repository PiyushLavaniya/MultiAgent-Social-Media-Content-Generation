from crewai import Task

generate_linkedin_post = {
    "description": """Create a professional and insightful LinkedIn post based on industry, company info, and product details.
        Ensure it's structured, valuable, and positions the company as an industry leader.
        Industry: {industry}
        Company Info: {company_info}
        Product Info: {product_info}""",
    "expected_output": "A well-structured LinkedIn post (3-5 paragraphs) with an industry-focused professional tone."
}

generate_twitter_post = {
    "description": """Write an engaging and concise Twitter post. It can be a single tweet or a short thread.
        Ensure it's engaging, follows Twitter best practices, and uses relevant hashtags.
        Industry: {industry}
        Company Info: {company_info}
        Product Info: {product_info}""",
    "expected_output": "A single tweet or a short thread (max 280 characters per tweet) that is engaging and shareable."
}

generate_instagram_post = {
    "description": """Create a catchy and trendy Instagram caption with relevant hashtags.
        Ensure it's engaging and aligns with the brand’s personality.
        Industry: {industry}
        Company Info: {company_info}
        Product Info: {product_info}""",
    "expected_output": "A fun and engaging Instagram caption with relevant hashtags."
}

generate_facebook_post = {
    "description": """Write a conversational and engaging Facebook post that resonates with the audience.
        The post should be friendly, engaging, and possibly include a call-to-action.
        Industry: {industry}
        Company Info: {company_info}
        Product Info: {product_info}""",
    "expected_output": "A well-crafted Facebook post (3-4 paragraphs) with a conversational tone."
}

humanize_post = {
    "description": """Refine and enhance the generated post to ensure it sounds natural, engaging, and human-like.
        Improve the readability, emotional connection, and engagement.""",
    "expected_output": "A polished version of the social media post with improved readability and engagement."
}

review_final_post = {
    "description": """Conduct a final review of the post to ensure clarity, engagement, and platform optimization.
        Verify the tone, grammar, and overall effectiveness before publishing.""",
    "expected_output": "The final, reviewed social media post ready for publishing."
}
