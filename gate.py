class Gate :
    def __init__(self, name: str, inputs: int, outputs: int) :
        self.__name = name
        self.__inputs = inputs
        self.__outputs = outputs
        

    def get_inputs(self) -> int:
        return self.__inputs
    
    def get_outputs(self) -> int :
        return self.__outputs


    def get_name(self) -> str:
        return self.__name
    
    def __str__(self) :
        return f"{self.__name} {self.__inputs} {self.__outputs}"
