import logging
from logging.handlers import RotatingFileHandler  # Auto-rotate log files when they reach a certain size.


# Здесь задана глобальная конфигурация для логирования:
logging.basicConfig(    
    encoding='utf-8',
    filename='main.log',
    filemode='w',
    format='%(asctime)s [%(levelname)s] %(filename)s:%(lineno)d - %(message)s',
    level=logging.DEBUG,  # Default: logging.WARNING
    force=True
)

# Здесь установлены настройки логгера для текущего файла - log.py.
logger = logging.getLogger(__name__)
# Устанавливаем уровень, с которого логи будут сохраняться в файл:
logger.setLevel(logging.INFO)

# Указываем обработчик логов:
handler = RotatingFileHandler(
    'my_logger.log',
    maxBytes=50000000,
    backupCount=5,
    encoding='utf-8'
)
# Создаём форматер:
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
# Применяем его к хендлеру:
handler.setFormatter(formatter)

# Добавляем хендлер в логгер:
logger.addHandler(handler)

# Примеры логирования различных уровней.
logger.debug('123')  # Когда нужна отладочная информация.
logger.info('Сообщение отправлено')  # Когда нужна дополнительная информация.
logger.warning('Большая нагрузка!')  # Когда что-то идёт не так, но работает.
logger.error('Бот не смог отправить сообщение')  # Когда что-то сломалось.
logger.critical('Всё упало! Зовите админа!1!111')  # Когда всё совсем плохо.
