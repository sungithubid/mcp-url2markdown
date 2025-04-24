from urllib.parse import urlparse

from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai.content_filter_strategy import PruningContentFilter
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator
from mcp.server.fastmcp import FastMCP

server = FastMCP("url2markdown MCP Server")


@server.tool()
async def URL2markdown(url: str) -> str:
    """
    把网页转为markdown。

    Args:
        url (str): 网站地址。
    Returns:
        content (str): 处理后的markdown格式内容。
    """

    if not validate_url(url):
        raise ValueError("Invalid URL format")

    result = await crawl(url)
    if result.success:
        content = result.markdown.fit_markdown
    else:
        raise ValueError(result.error_message)

    return content


def validate_url(url: str) -> bool:
    """Validate URL format."""
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


async def crawl(url: str) -> any:
    # Step 1: Create a pruning filter
    prune_filter = PruningContentFilter(
        # Lower → more content retained, higher → more content pruned
        threshold=0.45,
        # "fixed" or "dynamic"
        threshold_type="fixed",
        # Ignore nodes with <5 words
        # min_word_threshold=5,
    )

    # Step 2: Insert it into a Markdown Generator
    md_generator = DefaultMarkdownGenerator(content_filter=prune_filter)

    # Step 3: Pass it to CrawlerRunConfig
    config = CrawlerRunConfig(markdown_generator=md_generator)

    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url=url,
            config=config,
        )

        return result


if __name__ == "__main__":
    server.run()
