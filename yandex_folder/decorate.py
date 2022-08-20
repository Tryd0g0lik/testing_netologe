
# def parametrized_decoder(path_to_log = "files/log.txt"):
def parametrized_decoder(path_to_log = "files/log.txt"):
  def decorator_logo(fun):
    def wrapper(*args, **kwargs):
      import logging
      import pathlib

      import datetime
      log = {}
      fmt = "%Y-%m-%d %H:%M:%S"
      time_start = datetime.datetime.now().strftime(fmt)
      name_fun = fun.__name__
      pesponse = tuple(fun(*args, **kwargs))


      log["time_start_fun"] = time_start
      log["fun-name"] = name_fun
      if pesponse:
        log["response_fun"] = "Code: 200"
        current_dir = pathlib.Path.cwd()
        log['path'] = current_dir

      else:
        log["response_fun"] = "Code: 400"
      current_dir = pathlib.Path.cwd()
      log['path'] = current_dir

      try:
        logging.basicConfig(filename=path_to_log, level = logging.DEBUG)

        logging.info(log)
        logging.BASIC_FORMAT(log)
        logging.debug(log)
      except Exception:
        logging.basicConfig(filename="files/log.txt", level=logging.INFO)

        logging.info(log)
        logging.debug(log)
      finally:
        ...
      return pesponse

    return wrapper
  return decorator_logo