import weka.core.jvm as jvm
import sys
import traceback
from weka.core.converters import Loader
import weka.core.serialization as serialization
from weka.classifiers import Classifier
from weka.filters import Filter, MultiFilter

# Fuentes:
# https://github.com/fracpete/python-weka-wrapper-examples/blob/master/src/wekaexamples/classifiers/output_class_distribution.py
# http://pythonhosted.org/python-weka-wrapper/examples.html


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
    
    #ifileName = "featureVectorsEntrenamientoWithTopicRetuitFav_preprocesado.csv"
    ifileName = "predictMe.csv"
    modelFilename = "naivebayes.model"
    out = predictWithWeka(ifileName,modelFilename)
    print out


if __name__ == "__main__":
    try:
        jvm.start()
        jvm.start(system_cp=True, packages=True)
        main()
    except Exception, e:
        print(traceback.format_exc())
    finally:
        jvm.stop()