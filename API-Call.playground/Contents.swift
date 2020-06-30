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

let url = URL(string: "http:127.0.01:5000/store")!
var request = URLRequest(url: url)
request.httpMethod = "GET"

let task = URLSession.shared.dataTask(with: request) { data, _, _ in
    do {
        let store = try JSONDecoder().decode(Stores.self, from: data!)
        print(String(describing: store))
    } catch {
        fatalError()
    }
}
task.resume()
