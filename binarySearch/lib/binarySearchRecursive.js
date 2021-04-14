export class BinarySearch{
  constructor(){
  }
  binarySearch(list, search){
    list.sort(function(a,b){
      return a - b
    })
    return this.search(0, null, list.length, search, list)
  }

  search(low, mid, high, search, list){
    mid = Math.floor(low + (high-low)/2)

    if(list[mid] == search){
      return true
    }
    if(low > high){
      return false
    }

    if(search > list[mid]){
      return this.search(mid+1, mid, high, search, list)
    }
    if(search < list[mid]){
      return this.search(low, mid, mid-1, search, list)
    }
  }
}
