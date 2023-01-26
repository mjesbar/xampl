#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <sstream>


auto main() -> int {
    
    double value = 1996.9229123721931237219388;
    double* ptr = &value;
    double& ref = value;
    
    std::cout<<"value   : "<<std::setprecision(10)<<value<<std::endl;
    std::cout<<"&value  : "<<std::setprecision(10)<<&value<<std::endl;
    std::cout<<"ptr     : "<<std::setprecision(10)<<ptr<<std::endl;
    std::cout<<"*ptr    : "<<std::setprecision(10)<<*ptr<<std::endl;
    std::cout<<"ref     : "<<std::setprecision(10)<<ref<<std::endl;
    std::cout<<"&ref    : "<<std::setprecision(10)<<&ref<<std::endl;


    return 0;
}

