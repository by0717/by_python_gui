import asyncio


class test_1:
    def __init__(self):
        # 测试编号
        self.a = 1

    @staticmethod
    async def test_1_1():
        print("test_1_1")
        await asyncio.sleep(1)
        return True

    @staticmethod
    async def main_1(logger, log_widget):
        logger.log("Main_1 is testing", log_widget)
        await asyncio.sleep(10)
        logger.log("test_1 is testing", log_widget)
        await test_1.test_1_1()
        logger.log("main_1 is finished", log_widget)
        return True
