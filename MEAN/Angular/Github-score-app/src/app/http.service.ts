import { Injectable } from '@angular/core';
import { Http } from '@angular/http';
import 'rxjs/Rx'; //Injectable

@Injectable()

export class HttpService {
    constructor(private _http: Http) { }
      gitScore(username){
        return this._http.get('https://api.github.com/users/'+ username).map(data=>data.json()).toPromise();
}
}
