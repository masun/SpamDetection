import weka.core.jvm as jvm
import sys
import traceback
from weka.core.converters import Loader
import weka.core.serialization as serialization
from weka.classifiers import Classifier
from weka.filters import Filter, MultiFilter
from extractor_de_features import Tweet,TweetFeatureExtractor

# Fuentes:
# https://github.com/fracpete/python-weka-wrapper-examples/blob/master/src/wekaexamples/classifiers/output_class_distribution.py
# http://pythonhosted.org/python-weka-wrapper/examples.html

topics =   {0:'video chavista periodista sentada dtb'.split(" "),\
            1:'venezuela vivo cnn soyfdelrincon senal'.split(" "),\
            2:'trump donald mes opinion mexico'.split(" "),\
            3:'muerte dolares angeles prostitutas venden'.split(" "),\
            4:'ecuador vuelta cne lomasvisto resultados'.split(" "),\
            5:'uu ee indocumentados inmigrantes aissami'.split(" "),\
            6:'sports illustrated 2017 rubia portada'.split(" "),\
            7:'fotos lomasvisto anos accesorios orgullo'.split(" "),\
            8:'muere brutal embarazada companeras recibir'.split(" "),\
            9:'jong kim nam muerte corea'.split(" ")}


def asignarTopico(tweetText):
    palabras = tweetText.split(" ")
    puntuacion = [0 for i in topics]
    maxIndx = 0
    maxim = 0
    for indxT in topics :
        for palabra in palabras :
            for topWord in topics[indxT]:
                if topWord == palabra :
                    puntuacion[indxT] += 1
                    if puntuacion[indxT] > maxim :
                        maxim = puntuacion[indxT]
                        maxIndx = indxT
                
    return maxIndx



def construirFeature(tweetText, tweet_id,favorite_count,retweet_count) :
    idTopico = asignarTopico(tweetText)
    tweet = Tweet(tweetText, tweet_id,favorite_count,retweet_count)
    extractor = TweetFeatureExtractor(tweet_id)
    extractor.extractFeatures(tweet)
    featureVector = extractor.getFetureVector()
    featureVector["topic_id"]=idTopico
    featureVector["spam"] = 'n' if tweet_id % 2 else 'y'
    return featureVector


def predictWithWeka(csvFilenameWithInputToPredict,modelFilename):
    """
    #   Nota: para usar sin conocer la clase, se puede colocar una clase dummy
    #   e ignorar los valores actual y error de @return results.
    #
    #   Nota: es necesario que el archivo de nombre @csvFilenameWithInputToPredict
    #   contenga instancias de ambas clases (spam y sanas)
    #
    #   @csvFilenameWithInputToPredict : nombre del archivo csv con las instancias
    #                                   a predecir.
    #
    #   @modelFilename : nombre del archivo de modelo generado por weka y 
    #                    compatible con el archivo csv de entrada
    #
    #   @return results : lista de diccionarios con los siguientes indices
    #                      index, actual, predicted, error y distribution
    """
    loader = Loader(classname="weka.core.converters.CSVLoader")
    cls = Classifier(jobject=serialization.read(modelFilename))
    print(cls)
    
    data = loader.load_file(csvFilenameWithInputToPredict)
    data.class_is_last()
    
    multi = MultiFilter()
    remove = Filter(classname="weka.filters.unsupervised.attribute.Remove", options=["-R", "first"])
    numericToNom = Filter(classname="weka.filters.unsupervised.attribute.NumericToNominal", options=["-R","8,11"])
    normalize = Filter(classname="weka.filters.unsupervised.attribute.Normalize",options=["-S","1.0","-T","0.0"])
    multi.filters = [remove, numericToNom, normalize]
    multi.inputformat(data)
    test = multi.filter(data)
    
    
    results = []
    for index, inst in enumerate(test):
        result = dict()
        
        pred = cls.classify_instance(inst)
        dist = cls.distribution_for_instance(inst)
        
        result["index"] = index+1
        result["actual"] = inst.get_string_value(inst.class_index)
        result["predicted"] = inst.class_attribute.value(int(pred))
        result["error"] = "yes" if pred != inst.get_value(inst.class_index) else "no"
        result["distribution"] = str(dist.tolist())
        
        results.append(result)
        print result
        
    return results

def main() :
    
    ifileName = "predictMe.csv"
    modelFilename = "naivebayes.model"
    out = predictWithWeka(ifileName,modelFilename)
    print out


if __name__ == "__main__":
    try:
        jvm.start()
        jvm.start(system_cp=True, packages=True)
        main()
        print construirFeature("Trump designa al teniente general McMaster como nuevo asesor presidencial https://t.co/8uyawU6Rae", 1,9,8)
    except Exception, e:
        print(traceback.format_exc())
    finally:
        jvm.stop()