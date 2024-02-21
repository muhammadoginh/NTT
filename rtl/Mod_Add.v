`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: Muhammad Ogin Hasanuddin
// 
// Create Date: 2024/02/07 10:49:42
// Design Name: 
// Module Name: Mod_Add
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module Mod_Add(
    input clk,
    input rstn,
    input [47:0] A,
    input [47:0] M,
    input [47:0] q,
    output reg [47:0] B
    );
    
    reg [48:0] Add;
    reg [48:0] Sub;
    wire sel;
    
    reg [47:0] in_A;
    reg [47:0] in_M;
    reg [47:0] in_q;
    reg [47:0] out_B;
    
    // reg input
    always @(posedge clk or negedge rstn)
    begin
        if (~rstn)
        begin
            in_A <= 0;
            in_M <= 0;
            in_q <= 0;
        end
        else
        begin
            in_A <= A;
            in_M <= M;
            in_q <= q;
        end
    end
    
    // ############# datapath way 1
//    assign Add = in_A + in_M;
//    assign Sub = Add - in_q;
//    and(sel, ~Add[48], Sub[48]);
////    nand(sel, ~Add[48], Sub[48]);
    
    
//    always @(*)
//    begin
//        if(sel)
//            out_B <= Add;
////            out_B <= Sub;
//        else
//            out_B <= Sub;
////            out_B <= Add;
//    end
    
    // ############# datapath way 2
    always @(*)
    begin
        Add = in_A + in_M;
        
        if (Add > in_q)
            Add = Add - in_q;
        out_B = Add;
    end
    
    // reg output
    always @(posedge clk or negedge rstn)
    begin
        if (~rstn)
        begin
            B <= 0;
        end
        else
        begin
            B <= out_B;
        end
    end
    
endmodule
