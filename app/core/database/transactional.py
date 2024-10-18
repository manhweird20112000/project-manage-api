# from functools import wraps
#
#
#
# class Transactional:
#     def __call__(self, func):
#         @wraps(func)
#         async def _transactional(*args, **kwargs):
#             try:
#                 result = await func(*args, **kwargs)
#                 await session.commit()
#             except Exception as e:
#                 await session.rollback()
#                 raise e
#
#             return result
#
#         return _transactional