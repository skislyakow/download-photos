import asyncio


async def make_archive() -> bytes:
    proc = await asyncio.create_subprocess_exec(
        "zip",
        "-r",
        "-",
        "photos",
        stdout=asyncio.subprocess.PIPE,
    )
    archive, errors = await proc.communicate()

    if proc.returncode != 0:
        raise RecursionError(errors.decode(errors="replace"))

    return archive


async def main() -> None:
    archive = await make_archive()

    print("размер архива:", len(archive), "байт")
    print("первые 4 байта", archive[:4])


if __name__ == "__main__":
    asyncio.run(main())
