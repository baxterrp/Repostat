import functools
import logging

logger = logging.getLogger(__name__)


def retry(max_attempts: int = 3, exclusions: tuple[type[Exception]] = (Exception,)):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if isinstance(e, exclusions):
                        raise
                    logger.warning(f"Attempt {attempt + 1} failed: {e}")
                    if attempt == max_attempts - 1:
                        logger.error(f"All attempts failed for {func.__name__}")
                        raise

        return wrapper

    return decorator
