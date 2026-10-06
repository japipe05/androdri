async def test_allows_three_then_blocks_fourth(limiter):
    for expected_remaining in (2, 1, 0):
        decision = await limiter.acquire("1.1.1.1")
        assert decision.allowed and decision.remaining == expected_remaining

    blocked = await limiter.acquire("1.1.1.1")
    assert not blocked.allowed
    assert blocked.retry_after_seconds == 3600


async def test_allows_again_after_one_hour(limiter, clock):
    for _ in range(3):
        await limiter.acquire("1.1.1.1")
    assert not (await limiter.acquire("1.1.1.1")).allowed

    clock.advance(3599)
    assert not (await limiter.acquire("1.1.1.1")).allowed

    clock.advance(2)
    assert (await limiter.acquire("1.1.1.1")).allowed


async def test_keys_are_independent(limiter):
    for _ in range(3):
        await limiter.acquire("a")
    assert (await limiter.acquire("b")).allowed


async def test_release_returns_quota(limiter):
    for _ in range(3):
        await limiter.acquire("a")
    await limiter.release("a")
    assert (await limiter.acquire("a")).allowed
