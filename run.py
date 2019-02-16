# -*- coding: utf-8 -*-
from fe import app


app.debug = True
app.logger.debug('A value for debugging')
app.run(host="0.0.0.0",port=5000,use_reloader=False)