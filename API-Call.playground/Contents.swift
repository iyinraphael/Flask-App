import Foundation

//var stores: [Any] = [
//    ["name" : "My Wonderful Store",
//     "items" : [
//        ["name" : "My Item",
//         "price" : 15.99]
//        ]
//    ]
//]

struct Store: Codable {
    var name: String
    var items: [Item]
    
    struct Item: Codable {
        var name: String
        var price: Double
    }
}

struct Stores: Codable {
    var stores: [Store]
}

let store = Store(name: "My Wonderful Store", items: [Store.Item.init(name: "My Item", price: 15.99)])
let exampleJson = Stores(stores: [store])

let url = URL(string: "http:127.0.01:5000/store")!
var request = URLRequest(url: url)
request.httpMethod = "POST"

let task = URLSession.shared.dataTask(with: request) { data, _, _ in
    
}
