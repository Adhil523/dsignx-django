//SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;
contract dsignx{
    string public name;
    uint256 public id;

    function setData(string memory _name, uint256 _id) public {
        name = _name;
        id=_id;
    }
    function retrieve() public view returns(uint256){
        return id;
    }
    function retrieve() public view returns(string){
        return name;
    }

}