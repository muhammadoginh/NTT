`timescale 1ns/1ps

module CLA_Generator (
    input [127:0] p,
    input [127:0] g,
    input Cin,
    output reg [127:0] Cout
);

    // for improvement we can manually generate CLA by generate from p and g without waiting for Cout
    // first style
    generate
        for (genvar i = 0; i < 128; i = i + 1) begin
            CLA_Gen cla_inst (p[i], g[i], (i == 0 ? Cin : Cout[i - 1]), Cout[i]);
        end
    endgenerate

    // second style
    // assign Cout[0] = G[0] | (P[0] & Cin);
    // assign Cout[1] = G[1] | (P[1] & (G[0] | (P[0] & Cin)));
    // assign Cout[2] = G[2] | (P[2] & (G[1] | (P[1] & (G[0] | (P[0] & Cin)))));
    // assign Cout[3] = G[3] | (P[3] & (G[2] | (P[2] & (G[1] | (P[1] & (G[0] | (P[0] & Cin)))))));
    // assign Cout[4] = G[4] | (P[4] & (G[3] | (P[3] & (G[2] | (P[2] & (G[1] | (P[1] & (G[0] | (P[0] & Cin)))))))));


endmodule

module CLA_Gen (
    input p,
    input g,
    input Cin,
    output Cout
);

    assign Cout = g | (p & Cin);
    
endmodule