# SearchById gringer test
 
from net.grinder.script.Grinder import grinder
from net.grinder.script import Test
from net.grinder.plugin.http import HTTPRequest
from HTTPClient import NVPair
 
searchByIdTest = Test(1, "Test SearchById")
 
json1 = '''{"ProductId":"123"}'''
 
class TestRunner:
    def __call__(self):
        if grinder.runNumber > 0 or grinder.threadNumber > 0:
            raise RuntimeError("Use limited to one thread, one run; "
                               "see Amazon Web Services terms and conditions")
 
        request = HTTPRequest(url="http://api-mirror.wide-eyes.it")
        searchByIdTest.record(request)
 
        bytes = request.POST('/v1/SearchById', json1, ( NVPair('Content-Type', 'application/json'),  NVPair('apikey', 'helloworld'), )).inputStream
 
        grinder.logger.info(str(bytes))