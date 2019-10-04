import ServerLogger
import DataManager.main as DataManager

logger = ServerLogger.Logger()
manager = DataManager.Manager(logger)
parser = DataManager.AutoParser(manager, logger)