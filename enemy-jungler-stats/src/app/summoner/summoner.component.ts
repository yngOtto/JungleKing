import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-summoner',
  templateUrl: './summoner.component.html',
  styleUrls: ['./summoner.component.css']
})
export class SummonerComponent implements OnInit {

  constructor(private http: HttpClient) { }

  ngOnInit(): void {
  }

  getSummonerInfo(summoner_name: string, region: string, api_key: string) {
    return this.http.get(`http://localhost:5000/summoner?summoner_name=${summoner_name}&region=${region}&api_key=${api_key}`);
  }
}
