# SearchById gringer test
 
from net.grinder.script.Grinder import grinder
from net.grinder.script import Test
from net.grinder.plugin.http import HTTPRequest
from HTTPClient import NVPair
 
searchByIdTest = Test(1, "Test SearchById")
 
json1 = '''{"ProductId":123}'''

static String convertStreamToString(java.io.InputStream is) {
    java.util.Scanner s = new java.util.Scanner(is).useDelimiter("\\A");
    return s.hasNext() ? s.next() : "";
}

 
class TestRunner:
    def __call__(self):
        request = HTTPRequest(url="http://api-mirror.wide-eyes.it")
        searchByIdTest.record(request)
 
        bytes = request.POST('/v1/SearchById', json1, ( NVPair('Content-Type', 'application/json'),  NVPair('apikey', 'helloworld'), )).inputStream

        s = new java.util.Scanner(bytes).useDelimiter("\\A");
        result = s.hasNext() ? s.next() : "";
        grinder.logger.info(str(result))